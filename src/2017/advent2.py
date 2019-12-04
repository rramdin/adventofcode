#!/usr/bin/python

import sys
import io

# The spreadsheet consists of rows of apparently-random numbers. To make sure
# the recovery process is on the right track, they need you to calculate the
# spreadsheet's checksum. For each row, determine the difference between the
# largest value and the smallest value; the checksum is the sum of all of these
# differences.
#
# For example, given the following spreadsheet:
#
#   5 1 9 5
#   7 5 3
#   2 4 6 8
#
#   - The first row's largest and smallest values are 9 and 1, and their
#     difference is 8.
#   - The second row's largest and smallest values are 7 and 3, and their
#     difference is 4.
#   - The third row's difference is 6.
#
#   In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

def calculateChecksum(f):
   checksum = 0
   for l in f:
      splt = l.split()
      low = None
      high = None
      for d in splt:
         d = int(d)
         if low == None:
            low = d
            high = d
         elif d < low:
            low = d
         elif d > high:
            high = d
      checksum += high - low
   return checksum

def calculateChecksum2(f):
   checksum = 0
   for l in f:
      splt = l.split()
      splt = [int(x) for x in splt]
      result = None
      for i in range(len(splt)):
         for j in range(len(splt)):
            if i == j: continue
            if splt[i] % splt[j] == 0:
               result = splt[i] / splt[j]
               break
         if result is not None:
            break
      if result is None:
         raise Exception("Invalid input")
      checksum += result
   return checksum

if __name__ == '__main__':
   if len(sys.argv) != 2:
      print 'usage: %s <file name>' % sys.argv[0]
      sys.exit(1)
   fname = sys.argv[1]
   with open(fname, 'r') as f:
      result = calculateChecksum(f)
      print 'result = %d' % result
   with open(fname, 'r') as f:
      result = calculateChecksum2(f)
      print 'result2 = %d' % result

