import sys

f = open(sys.argv[1], 'r')

s = f.read()

print (s.count('(') - s.count(')'))
