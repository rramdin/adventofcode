import re
import sys

class Ingredient:
   def __init__(self, s):
      s = re.split('[ :,]+', s)
      self.name = s[0]
      self.capacity = int(s[2])
      self.durability = int(s[4])
      self.flavor = int(s[6])
      self.texture = int(s[8])
      self.calories = int(s[10])

def simpleScore(c, d, f, t, cal):
   return reduce(lambda x,y: x * max(0,y), [c, d, f, t])

def score500Cal(c, d, f, t, cal):
   if cal != 500:
      return 0
   else:
      return simpleScore(c, d, f, t, cal)

def scoreCookie(ingredients, weights, fn):
   c = sum(map(lambda i,w: i.capacity * w, ingredients, weights))
   d = sum(map(lambda i,w: i.durability * w, ingredients, weights))
   f = sum(map(lambda i,w: i.flavor * w, ingredients, weights))
   t = sum(map(lambda i,w: i.texture * w, ingredients, weights))
   cal = sum(map(lambda i,w: i.calories * w, ingredients, weights))
   return fn(c, d, f, t, cal)

def genRatios(n, s):
   if n == 1:
      yield (s,)
   else:
      for i in xrange(s+1):
         for j in genRatios(n-1, s-i):
            yield (i,) + j

def getBestCookieScore(ingredients, fn):
   best = 0
   for ratios in genRatios(len(ingredients), 100):
      best = max(best, scoreCookie(ingredients, ratios, fn))
   return best

def process(f, fn):
   ingredients = []
   for s in f:
      s = s.strip()
      if s == '': continue
      ingredients.append(Ingredient(s))

   return getBestCookieScore(ingredients, fn)

def run(name, fn):
   f = open(name, 'r')
   print process(f, fn)

if __name__ == '__main__':
   fname = sys.argv[1]
   part = sys.argv[2]
   if part == '1':
      run(fname, simpleScore)
   elif part == '2':
      run(fname, score500Cal)
