import advent11
import testing

def test():
   tests = {
         'aaaaaaaa': 'aaaaaaab',
         'aaaaaaaz': 'aaaaaaba',
         'aaaaazzz': 'aaaabaaa',
         'zzzzzzzz': 'aaaaaaaa',
         }
   testing.runTests(advent11.incrementString, tests)

   tests = {
         'hijklmmn': False,
         'abbceffg': False,
         'abbcegjk': False,
         'abcdffaa': True,
         'ghjaabcc': True,
         }
   testing.runTests(advent11.checkValid, tests)

   tests = {
         'abcdefgh': 'abcdffaa',
         'ghijklmn': 'ghjaabcc',
         }
   testing.runTests(advent11.findNext, tests)

test()
