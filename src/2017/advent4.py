#!/usr/bin/python

import sys
import io

def countValid(f):
   valid = 0
   for l in f:
      splt = l.split()
      m = {}
      good = True
      for s in splt:
         if s in m:
            good = False
            break;
         m[s] = True
      if good:
         valid += 1
   return valid

def countValid2(f):
   valid = 0
   for l in f:
      splt = l.split()
      m = {}
      good = True
      for s in splt:
         s = ''.join(sorted(s))
         if s in m:
            good = False
            break;
         m[s] = True
      if good:
         valid += 1
   return valid

if __name__ == '__main__':
   if len(sys.argv) != 2:
      print 'usage: %s <file name>' % sys.argv[0]
      sys.exit(1)
   fname = sys.argv[1]
   with open(fname, 'r') as f:
      result = countValid(f)
      print 'result = %d' % result

   with open(fname, 'r') as f:
      result2 = countValid2(f)
      print 'result2 = %d' % result2

