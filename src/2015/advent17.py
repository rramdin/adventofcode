import itertools
import re
import sys

def getCombinationsNum(containers, target, num_containers):
   good = 0
   for p in itertools.combinations(containers, num_containers):
      total = sum(p)
      if total == target:
         good += 1
   return good

def getMinContainers(containers, target):
   for l in range(1, len(containers)+1):
      good = getCombinationsNum(containers, target, l)
      if good > 0:
         return good

def getCombinations(containers, target):
   good = 0
   for l in range(1, len(containers)+1):
      good += getCombinationsNum(containers, target, l)
   return good

def process(lines, eggnog, fn):
   containers = [int(i) for i in re.split('\s+', lines.strip())]
   return fn(containers, eggnog)

def run(name, eggnog, fn):
   f = open(name, 'r')
   print process(f.read(), eggnog, fn)

if __name__ == '__main__':
   fname = sys.argv[1]
   eggnog = int(sys.argv[2])
   part = sys.argv[3]
   if part == '1':
      run(fname, eggnog, getCombinations)
   elif part == '2':
      run(fname, eggnog, getMinContainers)
