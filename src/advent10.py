import sys

def lookAndSay(s):
   if len(s) < 1:
      return s

   current = s[0]
   num = 1
   result = ''

   for c in s[1:]:
      if c != current:
         result += '%d%c' % (num, current)
         num = 1
         current = c
      else:
         num += 1
   result += '%d%c' % (num, current)
   return result

def process(start, iterations):
   for _ in range(iterations):
      start = lookAndSay(start)
   return len(start)

if __name__ == '__main__':
    start = sys.argv[1]
    iterations = int(sys.argv[2])
    print process(start, iterations)
