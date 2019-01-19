
# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby
print(*[(len(list(count)), int(key)) for key, count in groupby(input())])
