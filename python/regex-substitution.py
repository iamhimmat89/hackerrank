
# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re
n = int(input())
for i in range(n):
    str1 = input()
    while ' && ' in str1 or ' || ' in str1:
        str1 = str1.replace(" && "," and ").replace(" || "," or ")
    print(str1)
	