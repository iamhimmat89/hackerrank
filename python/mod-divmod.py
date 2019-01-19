
# https://www.hackerrank.com/challenges/python-mod-divmod/problem

n, m = int(input()), int(input())
op = divmod(n,m)

for i in range(len(op)):
    print(op[i])

print(op)
