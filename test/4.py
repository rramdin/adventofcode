import advent4
import testing

def test():
    tests = {
            'abcdef': 609043,
            'pqrstuv': 1048970,
            }
    testing.runTests(lambda x: advent4.findMatch(x, '00000'), tests)

test()
