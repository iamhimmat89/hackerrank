
# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

    if a <= 10 ** 10 and a >= 1 and b <= 10 ** 10 and b >= 1:
        print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))

