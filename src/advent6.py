import sys
import re

length = 1000
width = 1000

def turnOn(b):
   return True
def turnOff(b):
   return False
def toggle(b):
   return not b

part1 = {
      'on': lambda x: 1,
      'off': lambda x: 0,
      'toggle': lambda x: (x+1)%2,
      'default': 0,
      }

part2 = {
      'on': lambda x: x+1,
      'off': lambda x: max(x-1, 0),
      'toggle': lambda x: x+2,
      'default': 0,
      }

def process(grid, config, s):
   s = s.replace('turn ', '')
   s = re.split('[ |,]', s)

   fn = config[s[0]]
   x1 = int(s[1])
   y1 = int(s[2])
   x2 = int(s[4])
   y2 = int(s[5])

   for y in range(y1,y2+1):
      for x in range(x1,x2+1):
         grid[y][x] = fn(grid[y][x])

def count(g):
   return reduce(lambda p,q: p+q, map(lambda a: reduce(lambda x,y: x+y, a), g))

def run(config, fname):
   f = open(fname, 'r')

   grid = []
   for _ in range(length):
      row = [];
      grid.append(row)
      for _ in range(width):
         row.append(config['default'])

   for s in f:
      s = s.strip()
      process(grid, config, s)

   print count(grid)
if __name__ == '__main__':
    fname = sys.argv[1]
    part = sys.argv[2]
    if part == '1':
       run(part1, fname)
    elif part == '2':
       run(part2, fname)

