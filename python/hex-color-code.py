
# https://www.hackerrank.com/challenges/hex-color-code/problem

import re
n = int(input())
for i in range(n):
    line = input()
    codes = [j for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})[\s:;,)]', line, re.I)]
    for code in codes:
        print(code)
		