
# https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
m_set = set(map(int, input().split()))

n = int(input())
n_set = set(map(int, input().split()))

result = sorted(m_set.symmetric_difference(n_set))

for i in range(len(result)):
    print(result[i])
	