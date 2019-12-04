#!/usr/bin/python

import sys
import io
import hashlib

def rebalance(state):
   max_value = max(state)
   index = state.index(max_value)
   state[index] = 0
   index += 1

   while max_value > 0:
      if index >= len(state):
         index = 0
      state[index] += 1
      max_value -= 1
      index += 1

def hash(state):
   return hashlib.md5(str(state)).hexdigest()

def findLoop(state):
   states = {}
   state_hash = hash(state)

   while state_hash not in states:
      print state
      states[state_hash] = len(states)
      rebalance(state)
      state_hash = hash(state)

   return len(states), len(states) - states[state_hash]

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
      print 'result mode 1 = %d, cycles = %d' % findLoop(l)

      #l = parse(lines)
      #print 'result mode 2 = %d' % jump2(l)

