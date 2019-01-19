
# https://www.hackerrank.com/challenges/zipped/problem

num_stud, num_sub = list(map(int, input().split()))
x = []

for i in range(num_sub):
    x.append(map(float, input().split()))

for j in zip(*x): 
    print(sum(j)/len(j))
	