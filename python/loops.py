
# https://www.hackerrank.com/challenges/python-loops/problem

if __name__ == '__main__':
    n = int(raw_input())

    if n >= 1 and n <= 20:
        for i in range(n):
            print(i ** 2)
    