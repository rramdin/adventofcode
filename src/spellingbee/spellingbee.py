import os
import time
import sys
import collections

DEFAULT_DICTIONARY = os.path.join(os.path.dirname(sys.argv[0]), 'dictionary.txt')
MIN_LENGTH = 4

class SpellingBee:
    # The dictionary is essentially a recursive map-of-maps, each level
    # representing a letter in a word. Any terminal node is marked.
    class Dictionary:
        def __init__(self):
            self.word = None
            self.next = [None] * 26

        # Inserts a new word into the dictionary. This should only be called on
        # a top-level Dictionary.
        def addWord(self, word):
            self._insert(word, word)

        # Inserts a partial (or full) word into a dictionary
        def _insert(self, letters, word):
            if not letters:
                self.word = word
            else:
                self.getNext(letters[0], create=True)._insert(letters[1:], word)

        # Gets the dictionary for the next letter, if it exists.
        def getNext(self, l, create=False):
            next_letter_index = ord(l) - ord('A')
            assert next_letter_index >= 0 and next_letter_index < len(self.next)
            if create and not self.next[next_letter_index]:
                self.next[next_letter_index] = SpellingBee.Dictionary()
            return self.next[next_letter_index]

    def __init__(self):
        self.dictionary = SpellingBee.Dictionary()
        self.dictionaryList = []

    def loadDictionary(self, path=DEFAULT_DICTIONARY):
        with open(path, 'r') as d:
            for word in d:
                word = word.strip()
                self.dictionary.addWord(word.upper())
                self.dictionaryList.append(word.upper())

    @staticmethod
    def isPangram(letters, word):
        for letter in letters:
            if letter not in word:
                return False
        return True

    def solve(self, letters, reqd_letters):
        words = []
        self._wordsForLetters(letters, reqd_letters, self.dictionary, words=words)
        return sorted(words)

    # Recurively finds all the words for a set of letters
    def _wordsForLetters(self, letters, reqd_letters, dictionary, words, word='', has_reqd=False):
        if dictionary.word:
            if len(dictionary.word) >= MIN_LENGTH and (has_reqd or not reqd_letters):
                words.append(dictionary.word)

        def doLetter(l, has_reqd):
            next = dictionary.getNext(l)
            if next:
                new_word = word + l
                self._wordsForLetters(letters, reqd_letters, next, words, new_word, has_reqd)

        for l in letters:
            doLetter(l, has_reqd)
        for l in reqd_letters:
            doLetter(l, True)
        return words

    @staticmethod
    def scoreGame(words, letters):
        total = 0
        pangrams = []
        for word in words:
            if len(word) == 4:
                total += 1
            elif len(word) > 4:
                total += len(word)
                if SpellingBee.isPangram(letters, word):
                    total += 7
                    pangrams.append(word)
        return total, pangrams

def hunt():
    # Plays every game of possible and prints the max score to a file. 

    bee = SpellingBee()

    tic = time.perf_counter()
    bee.loadDictionary()
    dictTime = time.perf_counter() - tic

    print("Dictionary Load Time: %fs" % (dictTime))

    # Find all combinations of letters that can produce a pangram
    GAME_LETTERS = 7
    combinations = set()
    for word in bee.dictionaryList:
        letters = set(word)
        if len(letters) == 7:
            combinations.add(''.join(sorted(letters)))

    print("Number of games:", len(combinations)*GAME_LETTERS)

    count = 0

    # Find all the combinations with a required letter
    games = []
    for letters in sorted(combinations):
        for i in range(GAME_LETTERS):
            game_letters = letters[:i] + letters[i+1:]
            game_reqd = letters[i]

            games.append((game_letters, game_reqd))

    # Store the results here
    results = [0]*len(games)

    # Play a game and report its score
    def playGame(game_letters, game_reqd):
        words = bee.solve(game_letters, game_reqd)
        score, _ = SpellingBee.scoreGame(words, game_letters)
        return score

    # Actually play the games now
    print("Playing %d games..." % len(games))
    for i in range(len(games)):
        count += 1

        score = playGame(*games[i])
        results[i] = score

        if count % 10000 == 0:
            print("Played %d games..." % count)

    # Organize the results by score so they can be outputted in sorted order
    final_results = collections.defaultdict(list)
    for i in range(len(games)):
        final_results[results[i]].append(games[i])

    # Finally, write the result to a file
    output_file_name = "/tmp/spellingbee.out"
    print("Writing to", output_file_name)
    with open(output_file_name, "w") as out:
        for i in sorted(final_results.keys()):
            for game in final_results[i]:
                out.write("%s %s %d\n" % (game[0], game[1], i))

# Solves a given Spelling Bee
def solve():
    if len(sys.argv) < 2:
        print("Usage: %s <letters> [reqd letter]" % sys.argv[0])
        sys.exit(1)

    letters = sys.argv[1].upper()
    if len(sys.argv) > 2:
        reqd = sys.argv[2].upper()
    else:
        reqd = ''

    bee = SpellingBee()

    tic = time.perf_counter()
    bee.loadDictionary()
    dictTime = time.perf_counter() - tic


    tic = time.perf_counter()
    words = bee.solve(letters, reqd)
    solveTime = time.perf_counter() - tic

    score, pangrams = SpellingBee.scoreGame(words, letters)

    print("Words")
    print("-----")
    for word in words:
        print(word)
    print()

    print("Pangrams: ", ",".join(pangrams))

    print("Max Score: %d Number of Pangrams: %d" % (score, len(pangrams)))
    print("Dictionary Load Time: %fs Solve Time: %fs" % (dictTime, solveTime))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        solve()
    else:
        hunt()
