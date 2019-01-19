
# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy as np
a=input()
b=[]
c=[]
for i in range(int(a)):
    A=list(map(int,input().split()) )
    b.append(A)
for i in range(int(a)):
    B=list(map(int,input().split()) )
    c.append(B)
print(np.dot(b, c))
