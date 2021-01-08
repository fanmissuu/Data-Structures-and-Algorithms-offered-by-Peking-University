
#1.有个数限制的整数划分.
#在考虑有限个数整数划分时，我们可以设状态dp[i][j]，表示将整数i划分成j个整数
#那么就有dp[i][j]=dp[i-j][j]+dp[i-1][j-1]。
#ddp[i-j][j]：和为i的j个不为1的整数相加有几个。因为它就等于和为i-j的j个整数相加的组合数目（把这j项每项+1）。
#dp[i-1][j-1]：和为i的j个整数且第j个整数为1相加有几种组合。它就等于和为i-1的j-1项整数相加的组合数目（每种组合最后+1，即增添一个为1的项）。
#i==j时，dp[i][j]=1; i<j时，dp[i][j]=0;j==1时，dp[i][j]=1.
import copy
while True:
    try:
        line = input()
    except EOFError:
        break
    line = line.split()
    N = int(line[0])
    k = int(line[1])
    dp1 = []
    dp11 = []
    for j in range(k+1):
        dp11.append(0)
    for i in range(N+1):
        dp1.append(copy.deepcopy(dp11))
    for i in range(1,N+1):
        for j in range(1,k+1):
            if j == 1:
                dp1[i][j] = 1
            if i == j:
                dp1[i][j] = 1
    #初始化dp1
    for i in range(3,N+1):
        for j in range(2,k+1):
            dp1[i][j] = dp1[i-j][j]+dp1[i-1][j-1]
    print(dp1[N][k])

    #2
    dp2 = []
    dp22 = []
    for j in range(N+1):
        dp22.append(0)
    for i in range(N+1):
        dp2.append(copy.deepcopy(dp22))
    for i in range(1,N+1):
        dp2[i][1] = 1
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i <= j:
                dp2[i][j] = 1 + dp2[i][i-1]
            else:
                dp2[i][j] = dp2[i-j][j-1] + dp2[i][j-1]
    print(dp2[N][N])

    #3
    dp3 = []
    dp33 = []
    for i in range(N+1):
        dp33.append(0)
    for i in range(N+1):
        dp3.append(copy.deepcopy(dp33))
    for i in range(1,N+1):
        dp3[i][1] = 1
    for i in range(N+1):
        for j in range(3,N+1,2):
            if i % 2 == 1:
                if i < j:
                    dp3[i][j] = dp3[i][i]
                elif i == j:
                    dp3[i][j] = 1 + dp3[i][i-2]
                else:
                    dp3[i][j] = dp3[i-j][j] + dp3[i][j-2]
            else:
                if i < j:
                    dp3[i][j] = dp3[i][i-1]
                if i == j:
                    dp3[i][j] = 1 + dp3[i][i-3]
                else:
                    dp3[i][j] = dp3[i-j][j] + dp3[i][j-2]
    if N % 2 == 1:
        print(dp3[N][N])
    else:
        print(dp3[N][N-1])


#2.划分为若干个不同整数。
#dp[i][j]:将i划分为不大于j的整数。
#dp[i][j] = dp[i-j][j-1] + dp[i][j-1]。分为划分数里有j的情况和无j的情况。
#dp[i-j][j-1]:可表示和为i，划分数里有j的情况 == 和为i-j且划分数不大于j-1的情况（每种划分情况第一项加上一个j）。
                                #如为划分数可以重复，则此式改为dp[i-j][j].
#dp[i][j-1]:将i划分为不大于j-1的整数，即划分数里无j的情况。
#当i<j时，dp[i][j] = dp[i][i];当i>j时，dp[i][j] = dp[i-j][j-1] + dp[i][j-1]；当i==j时，dp[i][j] = 1+dp[i][j-1]。
#dp[i][1] = 1

#3.划分为若干奇数
#与4117题划分为若干整数一样，只不过将j限定为奇数。
