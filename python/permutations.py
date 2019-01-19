
# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
word, per = list(map(str, input().split()))

print(*[''.join(i) for i in permutations(sorted(word),int(per))],sep='\n')
