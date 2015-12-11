import sys

bad_strings = ('i', 'o', 'l')
bad_map = dict((x,True) for x in bad_strings)

def run(pw):
   print "Find next password after '%s'" % (pw)
   next_pw = findNext(pw)
   print "Next password: %s" % (next_pw)

def incrementString(s):
   i = len(s)-1
   new = ""
   while i >= 0:
      c = s[i]
      if c == 'z':
         new = 'a' + new
         i -= 1
      else:
         new = chr(ord(c)+1) + new
         break
   else:
      return 'a' * len(s)

   new = s[:i] + new
   return new

def checkValid(s):
   # check for bad letters
   bad_cond = True
   for i in bad_strings:
      if i in s:
         return False

   # check pairs
   i = 0
   dupe_count = 0
   while i < (len(s) - 1):
      if s[i] == s[i+1]:
         dupe_count += 1
         i += 1
      if dupe_count >= 2:
         break
      i += 1
   else:
      return False

   # check for three increasing letters
   i = 0
   while i < (len(s) - 2):
      if ord(s[i]) + 1 == ord(s[i+1]) and ord(s[i]) + 2 == ord(s[i+2]):
         break;
      i += 1
   else:
      return False

   return True

def findNext(s):
   s = incrementString(s)
   while not checkValid(s):
      s = incrementString(s)
   return s

if __name__ == '__main__':
   pw = sys.argv[1]
   run(pw)


