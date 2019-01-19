
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

n = list(map(int, input().split()))
d = []
if n[0] >= 1 and n[0] <= 10000 and n[1] >= 1 and n[1] <= 100:
    for i in range(n[0]):
        d.append(input())

    for j in range(n[1]):
        item = input()
        if len(item) >= 1 and len(item) <= 100:
            found = False
            for k in range(len(d)):
                if d[k] == item:
                    found = True
                    print(k+1, end=" ")
            if found == False:
                print("-1", end=" ")
            print("")    
			