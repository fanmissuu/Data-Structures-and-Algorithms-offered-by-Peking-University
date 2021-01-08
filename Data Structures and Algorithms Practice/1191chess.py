import copy

def fun(n,x1,y1,x2,y2):
    MIN = 10000000
    if res[n][x1][y1][x2][y2] != -1:
        return res[n][x1][y1][x2][y2]
    if n == 1:
        t = calsum(x1,y1,x2,y2)
        res[n][x1][y1][x2][y2] = t * t
        return t * t
    for a in range(x1,x2):
        c = calsum(a+1,y1,x2,y2)
        e = calsum(x1,y1,a,y2)
        t = min(fun(n-1,x1,y1,a,y2)+c*c, fun(n-1,a+1,y1,x2,y2)+e*e)
        if MIN > t:
            MIN = t
    for b in range(y1,y2):
        c = calsum(x1,b+1,x2,y2)
        e = calsum(x1,y1,x2,b)
        t = min(fun(n-1,x1,y1,x2,b)+c*c, fun(n-1,x1,b+1,x2,y2)+e*e)
        if MIN > t:
            MIN = t
    res[n][x1][y1][x2][y2] = MIN
    return MIN


n = int(input())
line = 0
s = [[0,0,0,0,0,0,0,0,0]]
b1 = [0]
while line < 8:
    a1 = input().strip().split()
    for i in range(8):
        b1.append(int(a1[i]))
    s.append(copy.deepcopy(b1))
    line += 1
    b1 = [0]
# 读入n和初始board:s 9*9
eve_sum = [0,0,0,0,0,0,0,0,0]
summ = []
for i in range(9):
    summ.append(copy.deepcopy(eve_sum))
for i in range(1,9):
    for j in range(1,9):
        summ[i][j] = s[i][j] + summ[i-1][j] + summ[i][j-1] - summ[i-1][j-1]
#得到sum 9*9
def calsum(x1,y1,x2,y2):
    return summ[x2][y2] - summ[x1-1][y2] - summ[x2][y1-1] + summ[x1-1][y1-1]

res = []
for i1 in range(15):
    res.append([])
    for i2 in range(9):
        res[i1].append([])
        for i3 in range(9):
            res[i1][i2].append([])
            for i4 in range(9):
                res[i1][i2][i3].append([])
                for i5 in range(9):
                    res[i1][i2][i3][i4].append(-1)

x_ave = summ[8][8]/n
ans = pow(abs(fun(n,1,1,8,8) - n*pow(x_ave,2))/n,0.5)
print('{:.3f}'.format(ans))
