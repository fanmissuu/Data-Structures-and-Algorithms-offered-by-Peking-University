#超时
import copy

line = input().strip().split()
N = int(line[0])
M = int(line[1])
count = 0
all_charms = [[0,0]]
while count < N:
    charm = []
    line = input().strip().split()
    for i in line:
        charm.append(int(i))
    all_charms.append(copy.deepcopy(charm))
    count += 1
    #读入all_charm
dp1 = []
dp = []
for i in range(N+1):
    for j in range(M+1):
        dp1.append(0)
    dp.append(copy.deepcopy(dp1))
    dp1 = []
for i in range(all_charms[1][0],M+1):
    dp[1][i] = all_charms[1][1]
for i in range(2,N+1):
    for j in range(M+1):
        if j < all_charms[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-all_charms[i][0]]+all_charms[i][1], dp[i-1][j])
print(dp[N][M])
#01背包的状态转换方程 f[i,j] = Max{ f[i-1,j-Wi]+Pi( j >= Wi ),  f[i-1,j] }
