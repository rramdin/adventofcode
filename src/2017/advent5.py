#!/usr/bin/python

import sys
import io

def jump1(arr):
   steps = 0
   current = 0

   while current < len(arr) and current >= 0:
      offset = arr[current]

      arr[current] += 1
      current = current + offset
      steps += 1

   return steps

def jump2(arr):
   steps = 0
   current = 0

   while current < len(arr) and current >= 0:
      offset = arr[current]
      arr[current] += 1 - 2*int(offset>=3)
      current += offset
      steps += 1

   return steps

def parse(l):
   return [int(s) for s in l.split()]

if __name__ == '__main__':
   if len(sys.argv) != 2:
      print 'usage: %s <file name>' % sys.argv[0]
      sys.exit(1)
   fname = sys.argv[1]
   with open(fname, 'r') as f:
      lines = f.read()

      l = parse(lines)
      print 'result mode 1 = %d' % jump1(l)

      l = parse(lines)
      print 'result mode 2 = %d' % jump2(l)

