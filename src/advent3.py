import sys

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

if __name__ == '__main__':
    fname = sys.argv[1]
    num_walkers = int(sys.argv[2])
    run(fname, num_walkers)
