#优化了空间 变为一维数组  仍超时
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
dp = []
for i in range(M+1):
    dp.append(0)
for i in range(1,N+1):
    for j in range(M,all_charms[i][0]-1,-1):
        dp[j] = max(dp[j],dp[j-all_charms[i][0]]+all_charms[i][1])
print(dp[M])
#01背包的状态转换方程 f[i,j] = Max{ f[i-1,j-Wi]+Pi( j >= Wi ),  f[i-1,j] }
