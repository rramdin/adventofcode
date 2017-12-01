#!/usr/bin/python

from advent1 import performCaptcha

def test():
   def check(expected, result, s):
      if expected == result:
         print 'PASS %s ( %s == %s )' % (s, str(expected), str(result))
      else:
         print 'FAIL %s ( got: %s expected: %s )' % (s, str(result), str(expected))
   check(3, performCaptcha('1122'), '1122')
   check(4, performCaptcha('1111'), '1111')
   check(0, performCaptcha('1234'), '1234')
   check(9, performCaptcha('91212129'), '91212129')
   check(0, performCaptcha(''), 'Emtpy')
   check(0, performCaptcha('1'), 'Single value')


if __name__ == '__main__':
   test()
