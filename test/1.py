import testing
import advent1

def test():
    # Part 1
    tests = {
            '(())': 0,
            '()()': 0,
            '(((': 3,
            '(()(()(': 3,
            '))(((((': 3,
            '())': -1,
            '))(': -1,
            ')))': -3,
            ')())())': -3,
            }
    testing.runTests(advent1.count, tests)

    # Part 2
    tests = {
            ')': 1,
            '()())': 5,
            }
    testing.runTests(advent1.findBasement, tests)

test()
