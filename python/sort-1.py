
# https://www.hackerrank.com/challenges/python-sort-sort/problem

def takekth(elem):
    return elem[k]

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    k = int(input())

    rec = sorted(arr, key=takekth)
    for i in range(len(rec)):
        for j in range(len(rec[i])):
            print(rec[i][j], end=' ')
        print('')
    