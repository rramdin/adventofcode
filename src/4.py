import md5
import sys

key = sys.argv[1]
print "Finding coin for: " + key

def satisfies(key, i):
    v = key + str(i)
    m = md5.new(v)
    d = m.hexdigest()
    return d.startswith('00000')

i = 1
while not satisfies(key, i):
    i += 1

print i
