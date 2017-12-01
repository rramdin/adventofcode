import sys

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

if __name__ == '__main__':
    fname = sys.argv[1]
    part = sys.argv[2]
    if part == '1':
        run(fname, count)
    elif part == '2':
        run(fname, findBasement)


