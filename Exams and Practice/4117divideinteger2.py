#网上常用的思路。 ac
#dp[i][j]:将i划分为不大于j的整数。
#dp[i][j] = dp[i-j][j] + dp[i][j-1]。分为划分数里有j的情况和无j的情况。
#dp[i-j][j]:可表示和为i，划分数里有j的情况 == 和为i-j且划分数不大于j的情况（每种划分情况第一项加上一个j）。
                                                 #如为划分为若干不同整数，则此式改为dp[i-j][j-1].
#dp[i][j-1]:将i划分为不大于j-1的整数，即划分数里无j的情况。
#当i<j时，dp[i][j] = dp[i][i];当i>j时，dp[i][j] = dp[i-j][j] + dp[i][j-1]；当i==j时，dp[i][j] = 1+dp[i][j-1]。
#dp[i][1] = 1
import copy
while True:
    try:
        line = input()
    except EOFError:
        break
    n = int(line)
    dp = []
    dp1 = []
    for j in range(n+1):
        dp1.append(0)
    for i in range(n+1):
        dp.append(copy.deepcopy(dp1))
    for i in range(1,n+1):
        dp[i][1] = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i <= j:
                dp[i][j] = 1 + dp[i][i-1]
            else:
                dp[i][j] = dp[i-j][j] + dp[i][j-1]

    print(dp[n][n])
