
# https://www.hackerrank.com/challenges/py-check-subset/problem

n = int(input())

for i in range(n):
    num1, set1, num2, set2 = int(input()), set(input().split()), int(input()), set(input().split())
    print(set1.issubset(set2))    

	