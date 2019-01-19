
# https://www.hackerrank.com/challenges/word-order/problem

n = int(input())

d = {}
dist = 0
for i in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
        dist += 1

print(dist)
for key, value in d.items():
    print(value, end=' ')
	