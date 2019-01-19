
# https://www.hackerrank.com/challenges/py-if-else/problem

n = int(raw_input())

if n >= 0 and n <= 100:
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n <= 5 and n >= 2:
        print("Not Weird")
    elif n % 2 == 0 and n <= 20 and n >= 6:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
