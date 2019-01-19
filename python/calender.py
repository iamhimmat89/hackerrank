
# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar
m, d, y = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
