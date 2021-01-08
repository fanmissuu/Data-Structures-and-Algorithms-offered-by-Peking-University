#ac 完全自己独立完成。
while True:
    try:
        line = input()
    except EOFError:
        break
    n = int(line)
    s = []
    for i1 in range(n+1):
        s.append([])
        for i2 in range(n+1):
            s[i1].append(0)
    for i in range(1,n+1):
        for j in range(i,0,-1):
            if i == j:
                s[i][j] = 1
            else:
                s[i][j] = s[i-j][j] + s[i][j+1]
    print(s[n][1])
#  func(i,j)= func(i-j,j) + func(i,j+1)    i是此正整数，j是几个加数中最小的数。
