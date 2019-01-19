
# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    kevsc = 0
    stusc = 0
    vols = 'AEIOU'
    for i in range(len(string)):
        if string[i] in vols:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)

    if kevsc > stusc:
        print("Kevin",kevsc)
    elif kevsc < stusc:
        print("Stuart",stusc)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
	