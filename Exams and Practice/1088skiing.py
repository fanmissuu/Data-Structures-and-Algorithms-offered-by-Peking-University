#ac
import copy

def func(a,b):
    if res[a][b] != -1:
        return res[a][b]
    if h[a][b]<=h[a-1][b] and h[a][b]<=h[a+1][b] and h[a][b]<=h[a][b-1] and h[a][b]<=h[a][b+1]:
        res[a][b] = 1
        return res[a][b]
    maxmax = 1
    if h[a][b]>h[a-1][b] and 0<a-1<r+1 and 0<b<c+1:
        max1 = func(a-1,b)+1
        if max1>maxmax:
            maxmax = max1
    if h[a][b]>h[a+1][b] and 0<a+1<r+1 and 0<b<c+1:
        max2 = func(a+1,b)+1
        if max2>maxmax:
            maxmax = max2
    if h[a][b]>h[a][b-1] and 0<a<r+1 and 0<b-1<c+1:
        max3 = func(a,b-1)+1
        if max3>maxmax:
            maxmax = max3
    if h[a][b]>h[a][b+1] and 0<a<r+1 and 0<b+1<c+1:
        max4 = func(a,b+1)+1
        if max4>maxmax:
            maxmax = max4
    res[a][b] = maxmax
    return res[a][b]

line = input().strip().split()
r = int(line[0])
c = int(line[1])
count = 0
h0 = []
for i in range(c+2):
    h0.append(1000000000000)
h = []
h.append(copy.deepcopy(h0))
h1 = [1000000000000]
while count < r:
    hline = input().strip().split()
    for i in range(c):
        h1.append(copy.deepcopy(int(hline[i])))
    h1.append(1000000000000)
    h.append(copy.deepcopy(h1))
    h1 = [1000000000000]
    count += 1
h.append(copy.deepcopy(h0))
#读入h矩阵 且周围围一圈100000……

res1 = []
res = []
for i in range(c+2):
    res1.append(-1)
for i in range(r+2):
    res.append(copy.deepcopy(res1))

ans = 1
for i in range(1,r+1):
    for j in range(1,c+1):
        ans = max(ans,func(i,j))
print(ans)
