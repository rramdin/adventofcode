import advent3
import testing

def test():
    tests = {
            '>': 2,
            '^>v<': 4,
            '^v^v^v^v^v': 2,
            }
    testing.runTests(lambda x: advent3.walk(x,1), tests)

    tests = {
            '^>': 3,
            '^>v<': 3,
            '^v^v^v^v^v': 11,
            }
    testing.runTests(lambda x: advent3.walk(x,2), tests)

test()
