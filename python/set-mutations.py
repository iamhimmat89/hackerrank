
# https://www.hackerrank.com/challenges/py-set-mutations/problem

a = int(input())
a_set = set(map(int, input().split()))

n = int(input())

for i in range(1,n*2,2):
    cmd = list(map(str, input().split()))
    n_set = set(map(int, input().split()))
    if cmd[0] == 'update':
        a_set.update(n_set)
    elif cmd[0] == 'intersection_update':
        a_set.intersection_update(n_set)
    elif cmd[0] == 'difference_update':
        a_set.difference_update(n_set)
    elif cmd[0] == 'symmetric_difference_update':
        a_set.symmetric_difference_update(n_set)

print(sum(a_set))
