
# https://www.hackerrank.com/challenges/collections-counter/problem

n = int(input())
shoe_sizes = list(map(int, input().split()))

cust = int(input())
profit = 0
for i in range(cust):
    new_shoe_sizes = []
    buy = list(map(int, input().split()))
    brought = False
    for j in range(len(shoe_sizes)):
        if buy[0] == shoe_sizes[j] and brought == False:
            profit += buy[1]
            brought = True
        else:
            new_shoe_sizes.append(shoe_sizes[j])
    shoe_sizes = new_shoe_sizes

print(profit)

