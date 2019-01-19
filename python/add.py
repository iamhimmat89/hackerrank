
# https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
s = set()

for i in range(n):
    val = str(input())
    s.add(val)

print(len(s))
