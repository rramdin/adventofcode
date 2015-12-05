import md5
import sys
import testing

def satisfies(key, i, match):
    v = key + str(i)
    m = md5.new(v)
    d = m.hexdigest()
    return d.startswith(match)

def findMatch(key, match):
    i = 1
    while not satisfies(key, i, match):
        i += 1
    return i

def test():
    tests = {
            'abcdef': 609043,
            'pqrstuv': 1048970,
            }
    testing.runTests(lambda x: findMatch(x, '00000'), tests)

key = sys.argv[1]
if key == 'test':
    test()
else:
    match = sys.argv[2]
    print findMatch(key, match)
