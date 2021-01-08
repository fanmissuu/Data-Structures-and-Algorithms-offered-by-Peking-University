#ac  人人为我
while True:
    n = int(input())
    if n == 0:
        break
    while n != 0:
        s = []
        for i1 in range(n+1):
            s.append([])
            for i2 in range(n+1):
                s[i1].append(1)
        #n+1行  n+1列的s  初始化为1
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                s[i][j] = 0
        for i in range(2,n+1):
            for j in range(i//2,0,-1):
                s[i][j] = s[i-2*j][j] + s[i][j+1]
        print('{} {}'.format(n,s[n][1]))
        break
#j表示i的所有解中所有数大于等于j  即第一个数和最后一个数（因为对称）>=j
#1、将s[i][j] (i>=j>i/2) 内容预处理成1（因为对于j>i/2时 所有的s[i][j]都是1，如s[6][4]=s[6][5]=s[6][6]=1 只有（6）一个）。
#2、将s[i][j] (i<j) 内容预处理成0 （因为根据定义j不可能比i大。）
#3、将s[0][j] 内容预处理成1 （因为当需要调用s[0][j]时表示一个数拆成了完全相同的两个数，结果当然是一个了，）
#4、在for (i=2;i<=nax;i++)的每次循环中加入for (j=i/2;j>=1;j--)循环，每次逆推结果   因为计算s[i][j]时要用到s[i][j+1]所以从大到小遍历
#https://blog.csdn.net/jiangjiashi/article/details/7776560
