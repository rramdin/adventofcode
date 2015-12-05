import sys
import testing

def walk(s, num_walkers):
    walkers = []
    for i in range(num_walkers):
        walkers.append({'x':0, 'y':0})

    houses = {}
    houses[(0,0)] = True

    for i in range(len(s)):
        c = s[i]
        w = i % num_walkers
        if c == '>':
            walkers[w]['x'] += 1
        elif c == '<':
            walkers[w]['x'] -= 1
        elif c == '^':
            walkers[w]['y'] += 1
        elif c == 'v':
            walkers[w]['y'] -= 1
        houses[(walkers[w]['x'],walkers[w]['y'])] = True

    return len(houses)

def run(fname, num_walkers):
    f = open(fname, 'r')
    houses = walk(f.read(), num_walkers)
    print houses

def test():
    tests = {
            '>': 2,
            '^>v<': 4,
            '^v^v^v^v^v': 2,
            }
    testing.runTests(lambda x: walk(x,1), tests)

    tests = {
            '^>': 3,
            '^>v<': 3,
            '^v^v^v^v^v': 11,
            }
    testing.runTests(lambda x: walk(x,2), tests)

fname = sys.argv[1]
if fname == 'test':
    test()
else:
    num_walkers = int(sys.argv[2])
    run(fname, num_walkers)
