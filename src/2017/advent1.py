#!/usr/bin/python

import sys

# The captcha requires you to review a sequence of digits (your puzzle input)
# and find the sum of all digits that match the next digit in the list. The
# list is circular, so the digit after the last digit is the first digit in the
# list.
# For example:
#   - 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the
#     second digit and the third digit (2) matches the fourth digit.
#   - 1111 produces 4 because each digit (all 1) matches the next.
#   - 1234 produces 0 because no digit matches the next.
#   - 91212129 produces 9 because the only digit that matches the next one is
#     the last digit, 9.

def performCaptcha(captcha):
   if len(captcha) <= 1:
      return 0

   last = captcha[-1]
   result = 0
   for c in captcha:
      if c == last:
         result += int(c)
      last = c
   return result

def performCaptcha2(captcha):
   if len(captcha) <= 1:
      return 0

   result = 0
   for index in range(len(captcha)):
      reference_index = (index + len(captcha)/2) % len(captcha)
      if captcha[index] == captcha[reference_index]:
         result += int(captcha[index])

   return result

if __name__ == '__main__':
   if len(sys.argv) != 2:
      print 'usage: %s <input>' % sys.argv[0]
      sys.exit(1)
   captcha = sys.argv[1]
   result = performCaptcha(captcha)
   print 'result = %d' % result
   result = performCaptcha2(captcha)
   print 'result2 = %d' % result

