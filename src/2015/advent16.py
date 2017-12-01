import re
import sys

def addAunt(aunts, s):
   spec = {}
   s = re.split('[:,]+', s)

   aunts[s[0]] = spec
   i = 1
   while i < len(s):
      spec[s[i].strip()] = int(s[i+1])
      i += 2

def addSpec(spec, s):
   s = re.split('[: ]+', s)
   spec[s[0]] = int(s[1])

def part1Comp(aunt, spec, k):
   return (not k in aunt) or (spec[k] == aunt[k])

def part2Comp(aunt, spec, k):
   if not k in aunt:
      return True

   if k in ['cats', 'trees']:
      return aunt[k] > spec[k]
   elif k in ['pomeranians', 'goldfish']:
      return aunt[k] < spec[k]
   else:
      return spec[k] == aunt[k]

def findAunt(aunts, spec, comp):
   for a, s in aunts.iteritems():
      for k in spec:
         if not comp(s, spec, k):
            break
      else:
         return a

def process(dict_file, spec_file):
   aunts = {}
   spec = {}
   f = open(dict_file, 'r')
   for s in f:
      s = s.strip()
      addAunt(aunts, s)

   f = open(spec_file, 'r')
   for s in f:
      s = s.strip()
      addSpec(spec, s)

   print findAunt(aunts, spec, part1Comp)
   print findAunt(aunts, spec, part2Comp)

if __name__ == '__main__':
   dict_file = sys.argv[1]
   spec_file = sys.argv[2]
   process(dict_file, spec_file)
