#枚举。
#为了避免重复枚举，我们可以使用“由小枚举到大的策略”，即每次枚举都使i<=j<=h，那么i,j<=n/3; 限制枚举的范围，可以提高百分之六十的效率。
n = int(input())
for eve_n in range(n):
    v = int(input())
    ans = 1000000000000
    for i in range(1,int(v/3)+1):
        if v % i == 0:
            for j in range(i,int(v/3)+1):
                if v/i % j == 0:
                    s = int(i*j + v/i + v/j)
                    if s < ans:
                        ans = s
    print(ans*2)
