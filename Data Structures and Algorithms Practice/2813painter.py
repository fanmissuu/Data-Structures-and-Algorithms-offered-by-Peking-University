import copy
n = int(input())
count = 0
brick = []
a = []
for i in range(n+2):
    a.append(0)
brick.append(a)
while count < n:
    b = ','.join(input().strip()).replace('w','1').replace('y','0').split(',')
    c1 = []
    for i in range(n+2):
        c1.append(0)
    for i in range(n):
        c1[i+1] = int(b[i])
    brick.append(c1)
    count += 1
#变成n+1行 n+2列的0 1矩阵       w白1 点亮      y黄0 熄灭

paint = []
d = []
for i in range(n+2):
    d.append(0)
for i in range(n+1):
    paint.append(copy.deepcopy(d))
#得到初始paint矩阵 n+1行 n+2列 全为0

def guess(n,brick,paint):
    for r in range(1,n):
        for c in range(1,n+1):
            paint[r+1][c]=(brick[r][c]+paint[r][c]+paint[r-1][c]+paint[r][c-1]+paint[r][c+1])%2
    for c in range(1,n+1):
        if (brick[n][c] + paint[n][c] + paint[n-1][c] + paint[n][c-1] + paint[n][c+1]) % 2 != 0:
            return False
            break
    else:
        return True

count1 = 0
flag = 0
while guess(n,brick,paint) == False:
    count1 += 1
    if count1 == 2**n:
        flag = 1
        break
    paint[1][1] += 1
    c = 1
    while paint[1][c] > 1:
        paint[1][c] = 0
        c += 1
        paint[1][c] += 1

if flag == 1:
    print('inf')
else:
    paint_brisk = 0
    for line in paint:
        for i in range(1,n+1):
            if line[i] == 1:
                paint_brisk += 1
    print(paint_brisk)
