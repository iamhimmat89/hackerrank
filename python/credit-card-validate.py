
# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re
n = int(input())
pattern = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for i in range(n):
    card_no = input()
    if pattern.search(card_no):
        print("Valid")
    else:
        print("Invalid")
		