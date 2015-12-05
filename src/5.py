import sys

bad_strings = ('ab', 'cd', 'pq', 'xy')
bad_map = dict((x,True) for x in bad_strings)

f = open(sys.argv[1], 'r')

result = 0

for s in f:
    s = s.strip()
    
    # check vowel count
    vowel_count = 0
    for c in 'aeiou':
        vowel_count += s.count(c)
    if vowel_count < 3:
        continue

    # check pairs
    dupe_cond = False
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            dupe_cond = True
        if s[i]+s[i+1] in bad_map:
            continue

    if dupe_cond:
        result += 1

print result
