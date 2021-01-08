import copy

def func(a,b):
    if res[a][b] != -1:
        return res[a][b]
    if a == n:
        return triangle[a][b]
    else:
        ans = triangle[a][b] + max(func(a+1,b),func(a+1,b+1))
        res[a][b] = ans
        return ans

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
print(func(1,1))
