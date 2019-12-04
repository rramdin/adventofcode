#!/usr/bin/python

from advent1 import performCaptcha, performCaptcha2

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

   check(6,  performCaptcha2('1212'), '1212')
   check(0,  performCaptcha2('1221'), '1221')
   check(4,  performCaptcha2('123425'), '123425')
   check(12, performCaptcha2('123123'), '123123')
   check(4,  performCaptcha2('12131415'), '12131415')
   check(0,  performCaptcha2(''), 'Emtpy')

if __name__ == '__main__':
   test()
