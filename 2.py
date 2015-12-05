f = open('2.txt', 'r')

result = 0
for s in f:
    s = s.strip()
    d = (s.split('x'))
    d = map(lambda x: int(x), d)
    areas = (d[0]*d[1], d[0]*d[2], d[1]*d[2])
    min_side = reduce(lambda x,y: min(x,y), areas)
    total = reduce(lambda x,y: x+y, areas)*2 + min_side
    result += total

print result
