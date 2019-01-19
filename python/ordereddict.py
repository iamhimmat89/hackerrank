
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

Dict = OrderedDict()
for i in range(int(input())):
    item, sp, price = input().rpartition(' ')
    Dict[item] = Dict.get(item, 0) + int(price)
print(*[" ".join([item, str(price)]) for item, price in Dict.items()], sep="\n")

