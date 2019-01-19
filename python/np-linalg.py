
# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy as np
np.set_printoptions(legacy='1.13')
n=int(input())
a=np.array([input().split() for i in range(n)],float)
print(np.linalg.det(a))
