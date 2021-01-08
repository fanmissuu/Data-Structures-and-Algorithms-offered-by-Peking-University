#应该是对的  wrong answer（因为long long？）
def func(n,c):
    skipped = 0
    ans = []
    for iii in range(n+1):
        ans.append(0)
    used = []
    for ii in range(n+1):
        used.append(0)
    for i in range(1,n+1):     #在第i位的数字
        num = 0
        for k in range(1,n+1):   #长度为k
            if used[k] == 0:
                num += 1
                if i == 1:
                    skipped = C[n][num][up] + C[n][num][down]
                else:
                    if (k > ans[i-1] and i <= 2) or (k > ans[i-1] and ans[i-2] > ans[i]-1):
                        skipped = C[n-i+1][num][down]
                    if (k < ans[i-1] and i <= 2) or (k < ans[i-1] and ans[i-2] < ans[i]-1):
                        skipped = C[n-i+1][num][up]
                if skipped >= c:
                    break
                else:
                    c -= skipped
        used[k] = 'true'
        ans[i] = k
    for i in range(1,n+1):
        print('{}'.format(ans[i]),end=' ')
    print()

K = int(input())
count = 0
while count < K:
    line = input().strip().split()
    n = int(line[0])
    c = int(line[1])
    C = []
    up = 0
    down = 1
    for i1 in range(n+1):
        C.append([])
        for i2 in range(n+1):
            C[i1].append([])
            for i3 in range(2):
                C[i1][i2].append(0)
    C[1][1][up] = C[1][1][down] = 1
    for i in range(2,n+1):
        for k in range(1,i+1):
            for M in range(k,i):
                C[i][k][up] += C[i-1][M][down]
            for N in range(1,k):
                C[i][k][down] += C[i-1][N][up]
    func(n,c)
    count += 1
