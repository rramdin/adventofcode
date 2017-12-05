#!/usr/bin/python

from advent3 import calcDistance

def test():
   def check(expected, result, s):
      if expected == result:
         print 'PASS %s ( %s == %s )' % (s, str(expected), str(result))
      else:
         print 'FAIL %s ( got: %s expected: %s )' % (s, str(result), str(expected))
   check(0, calcDistance(1), '1')
   check(3, calcDistance(12), '12')
   check(2, calcDistance(23), '23')
   check(31, calcDistance(1024), '1024')


if __name__ == '__main__':
   test()
