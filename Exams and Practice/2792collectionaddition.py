#对  但超时
n = int(input().strip())
count = 0
while count < n:
    s = int(input().strip())
    a = int(input().strip())
    A1 = input().strip().split()
    A = []
    for i in A1:
        A.append(int(i))
    A = sorted(A)
    b = int(input().strip())
    B1 = input().strip().split()
    B = []
    for i in B1:
        B.append(int(i))
    B = sorted(B)
    #读入每组数据

    ans = 0
    for i in A:
        if i >= s:
            break
        for j in B:
            if j >= s:
                break
            if i + j ==s:
                ans += 1
            if i + j > s:
                break
    count += 1
    print(ans)
