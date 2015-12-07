import advent5
import testing

def test():
   # Part 1
   tests = {
         'ugknbfddgicrmopn': True,
         'aaa': True,
         'jchzalrnumimnmhp': False,
         'haegwjzuvuyypxyu': False,
         'dvszwmarrgswjxmb': False,
         }
   testing.runTests(advent5.check1, tests)

   # Part 2
   tests = {
         'qjhvhtzxzqqjkmpb': True,
         'xxyxx': True,
         'uurcxstgmygtbstg': False,
         'ieodomkazucvgmuy': False,
         }
   testing.runTests(advent5.check2, tests)

test()
