#ac 完全自己独立完成。
def func(i,j):
    if res[i][j] != -1:
        return res[i][j]
    if i == j:
        res[i][j] = 1
        return res[i][j]
    elif i < j:
        res[i][j] = 0
        return res[i][j]
    else:
        res[i][j] = func(i-j,j) + func(i,j+1)    #i是此正整数，j是几个加数中最小的数大于等于j。
        return res[i][j]


while True:
    try:
        line = input()
    except EOFError:
        break
    n = int(line)
    res = []
    for i1 in range(n+1):
        res.append([])
        for i2 in range(n+1):
            res[i1].append(-1)
    print(func(n,1))
