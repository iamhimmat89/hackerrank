
# https://www.hackerrank.com/challenges/any-or-all/problem

n, values = int(input()), input().split()
print(all([int(i)>0 for i in values]) and any([j == j[::-1] for j in values]))
