
# https://www.hackerrank.com/challenges/python-time-delta/problem

from dateutil import parser

def time_delta(t1, t2):
    d1 = parser.parse(t1.strip())
    d2 = parser.parse(t2.strip())
    print(abs(int((d2-d1).total_seconds())))

t = int(input())
for t_itr in range(t):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)
