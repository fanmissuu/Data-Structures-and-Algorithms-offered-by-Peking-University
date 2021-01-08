#ac  人人为我
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

for i in range(2,k+1):
    for j in range(1,i):
        if a[i] > a[j]:
            res[i] = max(res[i], res[j]+1)
print(max(res))
