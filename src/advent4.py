import md5
import sys

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

if __name__ == '__main__':
    key = sys.argv[1]
    match = sys.argv[2]
    print findMatch(key, match)
