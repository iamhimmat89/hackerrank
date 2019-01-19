
# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy as np
a,b = [np.array([input().split()],int) for _ in range(2)]
print(np.inner(a,b)[0][0],np.outer(a,b),sep="\n")
