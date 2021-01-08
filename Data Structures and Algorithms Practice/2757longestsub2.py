#我为人人 ac
N = int(input())
a1 = input().strip().split()
a = [0]
for i in a1:
    a.append(int(i))
#读入序列，并在最前面添加了一个0
k = len(a1)
res = []
for i in range(k+1):
    res.append(1)

for i in range(1,k):
    for j in range(i+1,k+1):
        if a[j] > a[i]:
            res[j] = max(res[j], res[i]+1)
print(max(res))
