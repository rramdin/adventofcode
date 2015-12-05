import sys
import testing

def findBasement(s):
    floor = 0
    for i in range(len(s)):
        c = s[i]
        updown = 1 if c == '(' else -1 if c == ')' else 0
        floor += updown
        if floor < 0:
            return i+1
    return 0

def count(s):
    return s.count('(') - s.count(')')

def run(name, fn):
    f = open(name, 'r')
    s = f.read()
    print fn(s)

# Testing
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
    testing.runTests(count, tests)

    # Part 2
    tests = {
            ')': 1,
            '()())': 5,
            }
    testing.runTests(findBasement, tests)

fname = sys.argv[1]
if fname == 'test':
    test()
else:
    part = sys.argv[2]
    if part == '1':
        run(fname, count)
    elif part == '2':
        run(fname, findBasement)


