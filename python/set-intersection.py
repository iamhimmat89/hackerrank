
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

stud1 = int(input())
rno1 = set(map(int, input().split()))

stud2 = int(input())
rno2 = set(map(int, input().split()))

result = rno1.intersection(rno2)
print(len(result))
