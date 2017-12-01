import sys

bad_strings = ('ab', 'cd', 'pq', 'xy')
bad_map = dict((x,True) for x in bad_strings)

def run(fn, fname):
   f = open(fname, 'r')
   result = 0
   for s in f:
       s = s.strip()
       if fn(s):
          result += 1
   print result

def check1(s):
    # check vowel count
    vowel_count = 0
    for c in 'aeiou':
        vowel_count += s.count(c)
    if vowel_count < 3:
        return False

    # check pairs
    dupe_cond = False
    bad_cond = True
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            dupe_cond = True
        if s[i]+s[i+1] in bad_map:
            bad_cond = False

    return dupe_cond and bad_cond

def check2(s):
   pair_cond = False
   repeat_cond = False


   def checkPairs(s):
      pairs = {}
      for i in range(len(s) - 1):
         sub = s[i] + s[i+1]
         if sub in pairs:
            if pairs[sub] < i-1:
               return True
         else:
            pairs[sub] = i
      return False

   if not checkPairs(s):
      return False

   def checkRepeats(s):
      for i in range(len(s) - 2):
         if s[i] == s[i+2]:
            return True
      return False

   return checkRepeats(s)

if __name__ == '__main__':
    fname = sys.argv[1]
    part = sys.argv[2]
    if part == '1':
       run(check1, fname)
    elif part == '2':
       run(check2, fname)


