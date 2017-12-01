import itertools
import re
import sys

def getWeight(weights, l, i):
   p1 = l[i]
   p2 = l[(i+1)%len(l)]
   return weights[(p1,p2)] + weights[(p2,p1)]

def getHappiness(weights, l):
   weight = 0
   for i in range(len(l)):
      weight += getWeight(weights, l, i)
   return weight

def getBestArrangement(names, weights):
   p = itertools.permutations(names)
   start = next(iter(names))
   best = None
   best_arrangement = None
   for l in p:
      if l[0] != start:
         break
      weight = getHappiness(weights, l)
      if (not best) or weight > best:
         best = weight
         best_arrangement = l
   return best_arrangement

def getBestInterrupted(names, weights):
   a = getBestArrangement(names, weights)

   least_weight = None

   for i in range(len(a)):
      weight = getWeight(weights, a, i)
      if (not least_weight) or weight < least_weight:
         least_weight = weight

   return getHappiness(weights, a) - least_weight

def getBestHappiness(names, weights):
   return getHappiness(weights, getBestArrangement(names, weights))

def process(f, fn):
   weights = {}
   names = []
   for s in f:
      s = re.split(' ', s.strip())
      p1 = s[0]
      direction = 1 if s[2] == 'gain' else -1
      weight = int(s[3]) * direction
      # get last string, strip off trailing period
      p2 = s[-1][:-1]
      weights[(p1,p2)] = weight
      if p1 not in names:
         names.append(p1)
   return fn(names, weights) 

def run(name, fn):
   f = open(name, 'r')
   print process(f, fn)

if __name__ == '__main__':
   fname = sys.argv[1]
   part = sys.argv[2]
   if part == '1':
      run(fname, getBestHappiness)
   elif part == '2':
      run(fname, getBestInterrupted)

