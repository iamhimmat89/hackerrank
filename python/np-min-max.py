
# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np
n, m = map(int, input().split())
arr = np.array([input().split() for i in range(n)],int)
print(np.max(np.min(arr, axis=1), axis=0))
