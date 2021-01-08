#runtime error   mn检查过 为什么和c写的一样  c就能ac
import copy
d = int(input())
n = int(input())
garbage = []
for bomb in range(n):
    line1 = input().strip().split()
    garbage1 = []
    for i in line1:
        garbage1.append(int(i))
    garbage.append(copy.deepcopy(garbage1))
#读入数据
garbage_row = sorted(garbage,key=lambda x:x[0])
garbage_col = sorted(garbage,key=lambda x:x[1])
#建立二维数组size为garbage_row[-1][0]+d+1行，garbage_row[-1][1]+d+1列。
ans = -1
map = []
map1 = []
num = 0
for i in range(garbage_row[-1][1]+d+3):
    map1.append(0)
for i in range(garbage_row[-1][0]+d+3):
    map.append(copy.deepcopy(map1))
for i in range(n):
    for row in range(garbage[i][0]-d,garbage[i][0]+d+1):
        if 0 <= row <= 1024:
            for col in range(garbage[i][1]-d,garbage[i][1]+d+1):
                if 0 <= col <= 1024:
                    map[row][col] += garbage[i][2]
                    if map[row][col] > ans:
                        ans = map[row][col]
                        num = 1
                    elif map[row][col] == ans:
                        num += 1
print('{} {}'.format(num,ans))
