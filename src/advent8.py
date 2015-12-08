import sys

def encode(s):
   result = '"'
   for c in s:
      if c == '"':
         result += '\\"'
      elif c == '\\':
         result += '\\\\'
      else:
         result += c
   result += '"'
   return len(result) - len(s)

def diff(s):
   total = len(s)
   assert(s[0] == '"')
   assert(s[len(s)-1] == '"')
   inner = s[1:-1]
   i = 0
   size = 0
   while i < len(inner):
      size += 1
      if inner[i] == '\\':
         i += 1
         if inner[i] == '"':
            i += 1
         elif inner[i] == '\\':
            i += 1
         elif inner[i] == 'x':
            i += 3
      else:
         i += 1
   return total - size

def run(fn, fname):
   f = open(fname, 'r')
   result1 = 0
   result2 = 0
   for s in f:
       s = s.strip()
       result1 += diff(s)
       result2 += encode(s)
   print result1
   print result2

if __name__ == '__main__':
    fname = sys.argv[1]
    run(diff, fname)


