import advent8
import testing

def test():
   # Part 1
   tests = {
         '""': 2,
         '"abc"': 2,
         '"aaa\\"aaa"': 3,
         '"\\x27"': 5,
         }
   testing.runTests(advent8.diff, tests)

   tests = {
         '""': 4,
         '"abc"': 4,
         '"aaa\\"aaa"': 6,
         '"\\x27"': 5,
         }
   testing.runTests(advent8.encode, tests)

test()
