import json
import numbers
import sys

def __sumAllNumbers(j, skip):
    if skip(j):
        return 0
    if isinstance(j, dict):
        return reduce(lambda s,v: s + __sumAllNumbers(j[v], skip), j, 0)
    elif isinstance(j, list):
        return reduce(lambda s,v: s + __sumAllNumbers(v, skip), j, 0)
    elif isinstance(j, numbers.Number):
        return j
    else:
        return 0

def skipRed(s):
    def skip(j):
        return isinstance(j, dict) and 'red' in j.values()
    j = json.loads(s)
    return __sumAllNumbers(j, skip)

def sumAllNumbers(s):
    j = json.loads(s)
    return __sumAllNumbers(j, lambda x: False)

def run(name, fn):
    f = open(name, 'r')
    s = f.read()
    print fn(s)

if __name__ == '__main__':
    fname = sys.argv[1]
    part = sys.argv[2]
    if part == '1':
        run(fname, sumAllNumbers)
    elif part == '2':
        run(fname, skipRed)

