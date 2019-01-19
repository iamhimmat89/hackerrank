
# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re
n = int(input())
for i in range(n):
    name, email = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email)
    if m:
        print(name,email)
		