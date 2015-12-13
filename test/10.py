import advent10
import testing

def test():
   # Part 1
   tests = {
         '1': len('11'),
         '11': len('21'),
         '21': len('1211'),
         '1211': len('111221'),
         '111221': len('312211'),
         }
   testing.runTests(lambda x: advent10.process(x, 1), tests)

test()
