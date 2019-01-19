
# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

s, k = input(), input()
if k in s:
    print(*[(i.start(), (i.start()+len(k)-1)) for i in re.finditer(r'(?={})'.format(k), s)], sep='\n')
else:
    print('(-1, -1)')
	