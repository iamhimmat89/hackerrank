
# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    if year >= 1900 and year <= 10 ** 5:
        leap = False
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        elif year % 4 == 0:
            leap = True
        return leap
    else:
        return 'Constraints violated'
      
  
year = int(raw_input())
print is_leap(year)
