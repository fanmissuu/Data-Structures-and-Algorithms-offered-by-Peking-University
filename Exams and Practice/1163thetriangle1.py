import copy

n = int(input())
res = []
eve_res = []
for i in range(n+1):
    eve_res.append(-1)
for i in range(n+1):
    res.append(copy.deepcopy(eve_res))
#res n+1行 n+1列 全为-1

count = 1
triangle = []
eve_row = []
for i in range(n+1):
    eve_row.append(0)
for i in range(n+1):
    triangle.append(copy.deepcopy(eve_row))
#triangle为n+1行 n+1列 全为0

while count < n+1:
    line = input().strip().split()
    for i in range(count):
        triangle[count][i+1] = int(copy.deepcopy(line[i]))
    count += 1
#读入triangle n+1行 n+1列

for i in range(1,n+1):
    res[n][i] = triangle[n][i]
for i in range(n-1,0,-1):
    for j in  range(1,n):
        res[i][j] = triangle[i][j] + max(res[i+1][j], res[i+1][j+1])
print(res[1][1])
