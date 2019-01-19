
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    n = int(input())

    if n >= 2 and n <= 5:
        marklst = []
        for i in range(n):
            name = input()
            score = float(input())
            marklst.append([name, score])

        if marklst[0][1] <= marklst[1][1]:
            low, second_low = marklst[0], marklst[1]
        elif marklst[0][1] > marklst[1][1]:
            low, second_low = marklst[1], marklst[0]
    
        for i in range(2, len(marklst)):
            if marklst[i][1] < second_low[1]:
                if marklst[i][1] < low[1]:
                    low, second_low = marklst[i], low
                elif marklst[i][1] != low[1]:
                    second_low = marklst[i]
            elif low[1] == second_low[1] and marklst[i][1] > second_low[1]:
                second_low = marklst[i]

        second_low_dup = []
        for j in range(len(marklst)):
            if second_low[1] == marklst[j][1]:
                second_low_dup.append(marklst[j][0])        
        
        second_low_dup.sort()
        for name in sorted(second_low_dup):
            print(name)
        
    else:
        print('constraints violated')
		
