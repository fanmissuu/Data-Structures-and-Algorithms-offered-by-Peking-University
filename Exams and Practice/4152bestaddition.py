#meng检查没问题   题目要求高精度计算所以未ac
import copy

def func(n,m):
    minmin = 1000000000000
    if res[n][m] != -1:
        return res[n][m]
    if m == 0:
        res[n][m] = int(line[0:n])
        return res[n][m]
    else:
        for i in range(m,n):
            min1 = func(i,m-1)+int(line[i:n])
            if min1 < minmin:
                minmin = min1
        res[n][m] = minmin
        return res[n][m]


while True:
    try:
        num = int(input().strip())
        line = input().strip()
    except EOFError:
        break
    res1 = []
    res = []
    for i in range(num+1):
        res1.append(-1)
    for i in range(len(line)+1):
        res.append(copy.deepcopy(res1))
    print(func(len(line),num))
