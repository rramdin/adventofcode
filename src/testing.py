import sys
import testing

def runTests(fn, tests):
    for k,v in tests.iteritems():
        result = fn(k)
        if result == v:
            print "PASS: '%s'" % (k)
        else:
            print "FALL: '%s' (got: %d; expected: %d)" % (k,result,v)
            sys.exit(1)

