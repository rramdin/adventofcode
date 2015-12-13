import advent12
import testing

def test():
    tests = {
            '[1,2,3]': 6,
            '{"a":2,"b":4}': 6,
            '[[[3]]]': 3,
            '{"a":{"b":4},"c":-1}': 3,
            '{"a":[-1,1]}': 0,
            '[-1,{"a":1}]': 0,
            '[]': 0,
            '{}': 0,
            }
    testing.runTests(advent12.sumAllNumbers, tests)

    tests = {
            '[1,2,3]': 6,
            '[1,{"c":"red","b":2},3]': 4,
            '{"d":"red","e":[1,2,3,4],"f":5}': 0,
            '[1,"red",5]': 6,
            }
    testing.runTests(advent12.skipRed, tests)

test()
