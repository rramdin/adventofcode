import re
import sys

class Reindeer:
   def __init__(self, name, speed, stamina, rest_time):
      self.name = name
      self.speed = speed
      self.stamina = stamina
      self.rest_time = rest_time
      self.last_distance = 0
      self.score = 0

   def getDistance(self, time):
      cycle_time = self.stamina + self.rest_time
      cycle_dist = self.speed * self.stamina

      # calculate time for completed cycle
      cycles = int(time/cycle_time)
      dist = cycles * cycle_dist

      # calculate time for partial cycle
      remaining = time % cycle_time
      remaining_active_time = min(remaining, self.stamina)
      dist += remaining_active_time * self.speed
      self.last_distance = dist
      return dist

   def incrementScore(self):
      self.score += 1

def getBestTraveled(reindeer, time):
   return reduce(lambda x,y: max(x, y.getDistance(time)), reindeer, 0)

def getBestPoints(reindeer, time):
   for t in range(1, time+1):
      # step everyone forward
      map(lambda r: r.getDistance(t), reindeer)

      # calculate best
      best = reduce(lambda x,y: max(x,y),
                    map(lambda x: x.last_distance, reindeer))

      # increment score for winners
      map(lambda x: x.incrementScore(),
          filter(lambda x: x.last_distance == best, reindeer))

   # return best score
   return reduce(lambda x,y: max(x, y), map(lambda x: x.score, reindeer))

def process(f, time, fn):
   reindeer = []
   for s in f:
      s = s.strip()
      if s == '': pass
      s = re.split(' ', s)
      name = s[0]
      speed = int(s[3])
      stamina = int(s[6])
      rest_time = int(s[13])
      reindeer.append(Reindeer(name, speed, stamina, rest_time))

   return fn(reindeer, time)

def run(name, time, fn):
   f = open(name, 'r')
   print process(f, time, fn)

if __name__ == '__main__':
   fname = sys.argv[1]
   time = int(sys.argv[2])
   part = sys.argv[3]
   if part == '1':
      run(fname, time, getBestTraveled)
   elif part == '2':
      run(fname, time, getBestPoints)
