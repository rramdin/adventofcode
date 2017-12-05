#!/usr/bin/python

import sys
import math

def calcDistance(num):
   width = int(math.ceil(math.sqrt(float(num))))
   if width % 2 != 0:
      width += 1
   corner = int(width**2)

   print "num", num
   print "width", width
   print "corner", corner

   x = 0
   y = 0

   step = width - 1

   x1 = max(width/2-1, 0)
   y1 = max(width/2-1, 0)
   print x1, y1

   if num >= corner - step:
      x = corner - num
      y = width - 1
      print "top"
   elif num >= corner - 2*step:
      x = width - 1
      y = num - (corner - 2*step)
      print "right"
   elif num >= corner - 3*step:
      x = num - (corner-3*step)
      y = 0
      print "bottom"
   elif num >= corner - 4*step:
      x = 0
      y = corner - 3*step - num
      print "left"

   print x,y

   return abs(x1-x) + abs(y1-y)

def part2(num):
   width = 2
   m = {}

   m[(0,0)] = 1

   new_val = 1

   n = 1
   x = 1
   y = 0

   while new_val < num:

      # calc sum of neighbors
      new_val = 0
      if (x-1,y-1) in m:
         new_val += m[(x-1,y-1)]
      if (x-1,y) in m:
         new_val += m[(x-1,y)]
      if (x-1,y+1) in m:
         new_val += m[(x-1,y+1)]
      if (x+1,y-1) in m:
         new_val += m[(x+1,y-1)]
      if (x+1,y) in m:
         new_val += m[(x+1,y)]
      if (x+1,y+1) in m:
         new_val += m[(x+1,y+1)]
      if (x,y-1) in m:
         new_val += m[(x,y-1)]
      if (x,y+1) in m:
         new_val += m[(x,y+1)]

      m[(x,y)] = new_val

      print "%d: (%d,%d) = %d" %(n, x, y, new_val)

      corner = width**2
      step = width - 1

      n += 1

      print "n=%d corner=%d step=%d" %(n, corner, step)
      if n >= corner - 4*step:
         if n >= corner - 3*step:
            if n >= corner - 2*step:
               if n >= corner - step:
                  x -= 1
                  print "top"
                  if n == corner:
                     width += 2
                     print "corner!"
               else:
                  y += 1
                  print "right"
            else:
               x += 1
               print "bottom"
         else:
            y -= 1
            print "left"
   return new_val


if __name__ == '__main__':
   if len(sys.argv) != 3:
      print 'usage: %s <input>' % sys.argv[0]
      sys.exit(1)
   num = int(sys.argv[1])
   mode = int(sys.argv[2])
   if mode == 1:
      result = calcDistance(num)
   elif mode == 2:
      result = part2(num)
   print 'result = %d' % result

