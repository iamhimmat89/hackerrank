
# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np
n, m, p = map(int, input().split())
print(np.array([input().split() for i in range(n+m)], int))
