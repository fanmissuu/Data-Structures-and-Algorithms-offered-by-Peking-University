#ac 递归
def func(k):
    if res[k] != -1:
        return res[k]
    if k == 1:
        res[k] = 1
        return res[k]

    else:
        flag = False
        for ii in range(1,k):
            if a[ii] < a[k]:
                flag = True
                res[k] = max(func(ii)+1,res[k])
        if not flag:
            res[k] = 1
        return res[k]

N = int(input())
a1 = input().strip().split()
a = [0]
for i in a1:
    a.append(int(i))
#读入序列，并在最前面添加了一个0
k = len(a1)
res = []
for i in range(k+1):
    res.append(-1)
maxmax = 1
for iii in range(1,k+1):
    if func(iii) > maxmax:
        maxmax = func(iii)
print(maxmax)
