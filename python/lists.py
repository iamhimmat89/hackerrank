
# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    n = int(input())

    output = []
    for i in range(n):
        cmd = list(map(str, input().split()))
        if cmd[0] == 'insert':
            output.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':    
            print(output)
        elif cmd[0] == 'remove':
            output.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            output.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            output.sort()
        elif cmd[0] == 'pop':
            output.pop()
        elif cmd[0] == 'reverse':
            output.reverse()
			