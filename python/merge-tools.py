
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    i = 0
    while i < len(string):
        substr = []
        for _ in range(k):
            if string[i] not in substr:
                substr.append(string[i])
            i += 1
        print("".join(c for c in substr))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
	