
# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
n = int(input())

if n > 0 and n <= 100:
    d = deque()
    for i in range(n):
        ops = str(input())
        ops = ops.lower()

        val = ops.split(' ')
        if val[0] == 'append':
            d.append(val[1])
        elif val[0] == 'pop':
            d.pop()
        elif val[0] == 'popleft':
            d.popleft()
        elif val[0] == 'appendleft':
            d.appendleft(val[1])

    for i in range(len(d)):
        print(d[i], end =" ")
		