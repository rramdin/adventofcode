import advent17
import testing

def test():
   tests = {
         ("20 15 10 5 5", 25): 4,
         }
   testing.runTests(lambda x: advent17.process(x[0], x[1],
      advent17.getCombinations), tests)
   tests = {
         ("20 15 10 5 5", 25): 3,
         }
   testing.runTests(lambda x: advent17.process(x[0], x[1],
      advent17.getMinContainers), tests)

test()
