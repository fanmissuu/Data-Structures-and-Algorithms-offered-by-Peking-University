#划分为k个整数。完全自己独立思考，与网上思路不相同。
def func1(N,k,j):   #j表示一系列正整数中最小的那个数大于等于j
    if res1[N][k][j] != -1:
        return res1[N][k][j]
    if j * k > N:
        res1[N][k][j] = 0
        return res1[N][k][j]
    elif j * k == N:
        res1[N][k][j] = 1
        return res1[N][k][j]
    elif k == 1 and N > j:
        res1[N][k][j] = 1
        return res1[N][k][j]
    else:
        res1[N][k][j] = func1(N-j,k-1,j) + func1(N,k,j+1)
        return res1[N][k][j]


while True:
    try:
        line = input()
    except EOFError:
        break
    line = line.split()
    N = int(line[0])
    k = int(line[1])
    res1 = []
    for i1 in range(N+1):
        res1.append([])
        for i2 in range(k+1):
            res1[i1].append([])
            for i3 in range(N+5):
                res1[i1][i2].append(-1)
    print(func1(N,k,1))
