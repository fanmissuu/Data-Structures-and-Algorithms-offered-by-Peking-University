#ac
def func(i,j):
    if res[i][j] != -1:
        return res[i][j]
    if i//2 < j <= i or i == 0:
        res[i][j] = 1
        return res[i][j]
    if j > i:
        res[i][j] = 0
        return res[i][j]
    if 1 <= j <= i//2:
        res[i][j] = func(i-j*2,j) + func(i,j+1)
        return res[i][j]

while True:
    n = int(input())
    if n == 0:
        break
    while n != 0:
        res = []
        for i1 in range(n+1):
            res.append([])
            for i2 in range(n+1):
                res[i1].append(-1)

        print('{} {}'.format(n,func(n,1)))
        break
