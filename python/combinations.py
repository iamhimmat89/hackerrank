
# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

word, per = list(map(str, input().split()))
for j in range(1,int(per)+1):
    print(*[''.join(i) for i in combinations(sorted(word),int(j))],sep='\n')
	