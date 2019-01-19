
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

word, per = list(map(str, input().split()))
print(*[''.join(i) for i in combinations_with_replacement(sorted(word),int(per))],sep='\n')
