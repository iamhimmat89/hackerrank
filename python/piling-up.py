
# https://www.hackerrank.com/challenges/piling-up/problem

n = int(input())

if n >= 1 and n <= 5:
    cube = []
    sizes = []
    for i in range(n):
        cube.append(int(input()))
        sizes.append(str(input()))

    for j in range(len(cube)):
        if cube[j] >= 1 and cube[j] <= 10 ** 5:
            cube_size = sizes[j].split(' ')

            if len(cube_size) > 2:
                flag = False
                max = cube_size[0]
                if cube_size[len(cube_size)-1] > max:
                    max = cube_size[len(cube_size)-1]
            
                mid = len(cube_size) // 2
                for k in range(mid):
                    if int(cube_size[k]) >= 1 and int(cube_size[k]) < 2 ** 31 and int(cube_size[len(cube_size)-k-1]) >= 1 and int(cube_size[len(cube_size)-k-1]) < 2 ** 31:
                        if int(cube_size[k+1]) > int(max) or int(cube_size[len(cube_size)-k-2]) > int(max):
                            if int(cube_size[k+1]) > int(cube_size[len(cube_size)-k-2]):
                                max = int(cube_size[k+1])
                            elif int(cube_size[len(cube_size)-k-2]) > int(cube_size[k+1]):
                                max = int(cube_size[len(cube_size)-k-2])
                            
                            flag = True
                            break
                        elif cube_size[k+1] > cube_size[k] and cube_size[len(cube_size)-k-2] > cube_size[len(cube_size)-k-1]:
                            flag = True
                        
                if flag:
                    print("No")
                else:
                    print("Yes")
            else:
                print("Yes")
				