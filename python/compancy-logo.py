
# https://www.hackerrank.com/challenges/most-commons/problem

import operator

s = input()
occ = {}
for i in range(len(s)):
    if s[i] in occ:
        occ[s[i]] += 1
    else:
        occ[s[i]] = 1

sorted_occ = sorted(sorted(occ.items(),key=operator.itemgetter(0)),key=operator.itemgetter(1),reverse=True)
for j in range(3):
    print(sorted_occ[j][0], sorted_occ[j][1])
	