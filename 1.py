
f = open('1.txt', 'r')

s = f.read()

print (s.count('(') - s.count(')'))
