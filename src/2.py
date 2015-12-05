import sys
import itertools
import testing

def getDimensions(s):
    s = s.strip()
    d = (s.split('x'))
    return map(lambda x: int(x), d)

def calculatePaper(d):
    areas = map(lambda x:x[0]*x[1], itertools.combinations(d, 2))
    min_area = reduce(lambda x,y: min(x,y), areas)
    return reduce(lambda x,y: x+y, areas)*2 + min_area

def calculateRibbon(d):
    perimeters = map(lambda x:2*(x[0]+x[1]), itertools.combinations(d, 2))
    min_perimeter = reduce(lambda x,y: min(x,y), perimeters)
    volume = reduce(lambda x,y: x*y, d)
    return min_perimeter + volume

def run(fname):
    f = open(fname, 'r')

    total_paper = 0
    total_ribbon = 0
    for s in f:
        d = getDimensions(s)
        total_paper += calculatePaper(d)
        total_ribbon += calculateRibbon(d)

    print 'Total paper: %s' % (total_paper)
    print 'Total ribbon: %s' % (total_ribbon)

def test():
    tests = {
            '2x3x4': [2,3,4],
            '1x1x10': [1,1,10],
            }
    testing.runTests(getDimensions, tests)

    tests = {
            (2,3,4): 58,
            (1,1,10): 43,
            }
    testing.runTests(calculatePaper, tests)

    tests = {
            (2,3,4): 34,
            (1,1,10): 14,
            }
    testing.runTests(calculateRibbon, tests)


fname = sys.argv[1]
if fname == 'test':
    test()
else:
    run(fname)
