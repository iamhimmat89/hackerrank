
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

num_student = int(input())
columns = list(map(str, input().split()))
marksheet = namedtuple('Student', columns)

marks = 0
for i in range(num_student):
    values = list(map(str, input().split()))
    rec = marksheet(values[0], values[1], values[2], values[3])
    marks += int(rec.MARKS)

print("{:.2f}".format(marks/num_student))
