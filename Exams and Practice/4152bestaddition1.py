#meng检查没问题   题目要求高精度计算所以未ac
import copy
while True:
    try:
        m = int(input().strip())
        line = input().strip()
    except EOFError:
        break
    res1 = []
    res = []
    for i in range(m+1):
        res1.append(0)
    for i in range(len(line)+1):
        res.append(copy.deepcopy(res1))


    for i in range(1,len(line)+1):
        res[i][0] = int(line[:i])


    for j in range(1, m+1):
        for i in range(j+1, len(line)+1):
            minmin = 100000000000000
            for s in range(j,i):
                min1 = res[s][j-1]+int(line[s:i])
                if min1 < minmin:
                    minmin = min1
            res[i][j] = minmin

    print(res[len(line)][m])
