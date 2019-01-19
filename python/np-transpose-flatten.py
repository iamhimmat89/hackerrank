
# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np
n, m = map(int, input().split())
arr = np.array([input().strip().split() for i in range(n)], int)
print (arr.transpose())
print (arr.flatten())
