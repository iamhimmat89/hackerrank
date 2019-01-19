
# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re
[print(bool(re.match(r'[-+]?[0-9]*\.[0-9]{1,}$',input()))) for i in range(int(input()))]
