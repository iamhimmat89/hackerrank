
# https://www.hackerrank.com/challenges/matrix-script/problem

import re

nm = input().split()
n = int(nm[0])
m = int(nm[1])
matrix = []
for _ in range(n):
    matrix_item = list(input())
    matrix.append(matrix_item)

final = []
for i in range(m):
    for j in range(n):
        final.append(matrix[j][i])

finalstr = "".join(final)
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", finalstr))
