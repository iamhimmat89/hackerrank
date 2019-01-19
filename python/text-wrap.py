
# https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(string, max_width):
    str1 = ''
    for i in range(0, len(string), max_width):
        str1 += string[i:i+max_width] + "\n"
    return str1

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
	