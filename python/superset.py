
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

set_a = set(map(int, input().split()))

flag = True
for i in range(int(input())):
    set_b = set(map(int, input().split()))
    if not set_a.issuperset(set_b):
        flag = False

print(flag)
