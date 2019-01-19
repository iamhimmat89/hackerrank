
# https://www.hackerrank.com/challenges/exceptions/problem

for i in range(int(input())):
    try:
        n,m = list(map(int,input().split()))
        print(n//m)
    except Exception as e:
        print("Error Code:",e)
		