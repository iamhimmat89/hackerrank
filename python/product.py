
# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product
a, b = list(map(int, input().split())), list(map(int, input().split()))

prod = list(product(a,b))
for i in range(len(prod)):
    print(prod[i], end=' ')
	