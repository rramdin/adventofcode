import advent10
import testing

def test():
   # Part 1
   tests = {
         '1': '11',
         '11': '21',
         '21': '1211',
         '1211': '111221',
         '111221': '312211',
         }
   testing.runTests(lambda x: advent10.process(x, 1), tests)

test()
