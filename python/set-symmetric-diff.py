
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

stud1 = int(input())
rno1 = set(map(int, input().split()))

stud2 = int(input())
rno2 = set(map(int, input().split()))

result = rno1.symmetric_difference(rno2)

print(len(result))
