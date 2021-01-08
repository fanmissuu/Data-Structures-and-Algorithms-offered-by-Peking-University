#应该是对的  但是超时了
import copy

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
    res1.append(1)
for i in range(r+2):
    res.append(copy.deepcopy(res1))

res_ans = copy.deepcopy(res)

while True:
    for i in range(1,r+1):
        for j in range(1,c+1):
            if h[i][j]<h[i-1][j] and h[i][j]<h[i+1][j] and h[i][j]<h[i][j-1] and h[i][j]<h[i][j+1]:
                res_ans[i][j] = 1
                continue
            maxmax = 1
            if h[i][j]>h[i-1][j] and 0<i-1<r+1 and 0<j<c+1:
                max1 = res[i-1][j]+1
                if max1>maxmax:
                    maxmax = max1
            if h[i][j]>h[i+1][j] and 0<i+1<r+1 and 0<j<c+1:
                max2 = res[i+1][j]+1
                if max2>maxmax:
                    maxmax = max2
            if h[i][j]>h[i][j-1] and 0<i<r+1 and 0<j-1<c+1:
                max3 = res[i][j-1]+1
                if max3>maxmax:
                    maxmax = max3
            if h[i][j]>h[i][j+1] and 0<i<r+1 and 0<j+1<c+1:
                max4 = res[i][j+1]+1
                if max4>maxmax:
                    maxmax = max4
            res_ans[i][j] = max(res[i][j],maxmax)
    if res_ans == res:
        break
    res = copy.deepcopy(res_ans)

ab = []
for i in res_ans:
    ab.append(max(i))
print(max(ab))
