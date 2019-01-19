
# https://www.hackerrank.com/challenges/no-idea/problem

nm = list(map(int, input().split()))
n  = nm[0]
m  = nm[1]
arr = list(map(int, input().split()))
A = set(map(int,input().split(' '))) 
B = set(map(int,input().split(' '))) 

happiness = 0
for i in range(n):
    if arr[i] in A:
        happiness += 1
    elif arr[i] in B:
        happiness -= 1
print(happiness)
