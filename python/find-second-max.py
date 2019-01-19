
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    if n >= 2 and n <= 10:
        arr = list(map(int, input().split()))

        if n == len(arr):
            if arr[0] >= -100 and arr[0] <= 100 and arr[1] >= -100 and arr[1] <= 100:
                if arr[0] >= arr[1]:
                    max, second_max = arr[0], arr[1]
                elif arr[0] < arr[1]:
                    max, second_max = arr[1], arr[0]

                constraints = True
                for i in range(2, len(arr)):
                    if arr[i] >= -100 and arr[i] <= 100:
                        if arr[i] > second_max:
                            if arr[i] > max:
                                max, second_max = arr[i], max
                            elif arr[i] != max:
                                second_max = arr[i]
                        elif max == second_max and arr[i] < second_max:
                            second_max = arr[i]
                    else:
                        constraints = False

                if constraints:
                    print(second_max)
            else:
                print('constraints violated')
        else:
            print('constraints violated')
    else:
        print('constraints violated')
		