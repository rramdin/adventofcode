#!/usr/bin/python

import sys
import io

def jump(arr, mode):
   steps = 0
   current = 0

   while current < len(arr) and current >= 0:
      offset = arr[current]

      if mode == 1:
         arr[current] += 1
      elif mode == 2:
         if offset >= 3:
            arr[current] -= 1
         else:
            arr[current] += 1
      current = current + offset
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
      print 'result mode 1 = %d' % jump(l, 1)

      l = parse(lines)
      print 'result mode 2 = %d' % jump(l, 2)

