import copy
def funcone(A,b,s):
    ans = 0
    for i in A:
        if i + b == s:
            ans += 1
        if i + b > s:
            break
    return ans

def func(A,B):
    if len(B) == 1:
        funcone(A,B[0])
    if B[-1]+A[0]>s or B[-1]+A[-1]<s:
        return func(A,B[:-1])
    else:
        return func(A,B[:-1]) + funcone(A,B[-1])





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
    res1 = []
    res = []
    print(func(A,B))
