#对  但超时
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
        return funcone(A,B[0],s)
    elif len(B) == 2:
        return funcone(A,B[0],s)+funcone(A,B[-1],s)
    else:
        if B[-1]+A[0]>s or B[-1]+A[-1]<s:
            return func(A,B[:-1])
        else:
            return func(A,B[:-1]) + funcone(A,B[-1],s)

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
    count += 1
    print(func(A,B))
