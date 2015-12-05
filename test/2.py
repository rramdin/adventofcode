import advent2
import testing

def test():
    tests = {
            '2x3x4': [2,3,4],
            '1x1x10': [1,1,10],
            }
    testing.runTests(advent2.getDimensions, tests)

    tests = {
            (2,3,4): 58,
            (1,1,10): 43,
            }
    testing.runTests(advent2.calculatePaper, tests)

    tests = {
            (2,3,4): 34,
            (1,1,10): 14,
            }
    testing.runTests(advent2.calculateRibbon, tests)

test()
