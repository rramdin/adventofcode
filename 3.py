import sys
f = open(sys.argv[1], 'r')

x = 0
y = 0

houses = {}

for c in f.read():
    if c == '>':
        x += 1
    elif c == '<':
        x -= 1
    elif c == '^':
        y += 1
    elif c == 'v':
        y -= 1
    houses[(x,y)] = True

print len(houses)
