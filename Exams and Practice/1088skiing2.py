#ac "人人为我"
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
#记录len的矩阵

sorting = []
sorting1 = []
for i in range(1,r+1):
    for j in range(1,c+1):
        sorting1.append(copy.deepcopy(i))
        sorting1.append(copy.deepcopy(j))
        sorting1.append(copy.deepcopy(h[i][j]))
        sorting.append(copy.deepcopy(sorting1))
        sorting1 = []
sorting = sorted(sorting,key = lambda x:x[2])
#按高度将所有点排序

for spot in sorting:
    if 0<spot[0]-1<r+1 and 0<spot[1]<c+1 and spot[2]>h[spot[0]-1][spot[1]] and res[spot[0]][spot[1]]<=res[spot[0]-1][spot[1]]:
        res[spot[0]][spot[1]] = res[spot[0]-1][spot[1]] + 1
    if 0<spot[0]+1<r+1 and 0<spot[1]<c+1 and spot[2]>h[spot[0]+1][spot[1]] and res[spot[0]][spot[1]]<=res[spot[0]+1][spot[1]]:
        res[spot[0]][spot[1]] = res[spot[0]+1][spot[1]] + 1
    if 0<spot[0]<r+1 and 0<spot[1]-1<c+1 and spot[2]>h[spot[0]][spot[1]-1] and res[spot[0]][spot[1]]<=res[spot[0]][spot[1]-1]:
        res[spot[0]][spot[1]] = res[spot[0]][spot[1]-1] + 1
    if 0<spot[0]<r+1 and 0<spot[1]+1<c+1 and spot[2]>h[spot[0]][spot[1]+1] and res[spot[0]][spot[1]]<=res[spot[0]][spot[1]+1]:
        res[spot[0]][spot[1]] = res[spot[0]][spot[1]+1] + 1
max_group = []
for i in res:
    max_group.append(max(i))
print(max(max_group))
