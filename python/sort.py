
# https://www.hackerrank.com/challenges/ginorts/problem

ip = input()
lc, uc, ed, od = [], [], [], []

for i in range(len(ip)):
    if ip[i].isdigit():
        if int(ip[i])%2 == 0:
            ed.append(int(ip[i]))
        else:
            od.append(int(ip[i]))
    elif ip[i].isupper():
        uc.append(ip[i])
    elif ip[i].islower():
        lc.append(ip[i])

lcs = sorted(lc)
ucs = sorted(uc)
ods = sorted(od)
eds = sorted(ed)
final = lcs + ucs + ods + eds

for j in range(len(final)):
    print(final[j], end='')

	