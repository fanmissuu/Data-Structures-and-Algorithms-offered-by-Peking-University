#完全自己独立编写  ac
def check(x):
    global C
    cow = 1
    now = barns[0]
    for i in range(1,len(barns)):
        if barns[i] - now >= x:
            cow += 1
            now = barns[i]
            if cow >= C:
                return True
    return False

line = input().strip().split()
N = int(line[0])
C = int(line[1])
barns = []
for barn in range(N):
    barns.append(int(input()))
barns = sorted(barns)
#读入所有数据 并把各个barn安位置排序
l = 100000000000
former = barns[0]
for i in range(1,len(barns)):
    if barns[i] - former < l:
        l = barns[i] - former
    former = barns[i]
r = barns[-1] - barns[0]
#l是最小间距  r是最大间距

if C == 2:
    print(r)
else:
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            l = mid + 1
        else:
            r = mid - 1
    print(r)
