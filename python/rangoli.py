
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    alpha = string.ascii_lowercase

    rangoli = []
    for i in range(size):
        s = "-".join(alpha[i:n])
        rangoli.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(rangoli[:0:-1]+rangoli))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
	