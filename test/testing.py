import sys
import testing

def runTests(fn, tests):
    for k,v in tests.iteritems():
        result = fn(k)
        if result == v:
            print "PASS: '%s'" % (str(k))
        else:
            print "FALL: '%s' (got: %s; expected: %s)" % (str(k), str(result),
                    str(v))
            sys.exit(1)

