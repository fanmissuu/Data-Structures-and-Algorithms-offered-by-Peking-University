a = input().strip().split()
r = int(a[0])
c = int(a[1])
N = int(input())
count = 0
spot = []
while count < N:
    n = input().strip().split()
    spot.append((int(n[0]),int(n[1])))
    count += 1
point = sorted(spot)
# 得到排序后的元组list

max = 2
steps = 2
for i in range(N-1):
    for j in range(1,N):
        dx = point[j][0] - point[i][0]
        dy = point[j][1] - point[i][1]
        if 1<=point[i][0]-dx<=r and 1<=point[i][1]-dy<=c:
            continue
        if point[i][0]+max*dx>r:
            break
        if point[i][1]+max*dy>c or point[i][1]+max*dy<1:
            continue
        while (point[i][0]+steps*dx,point[i][1]+steps*dy) in point:
            steps += 1
        if steps > max:
            max = steps

if max==2:
    print('0')
else:
    print(max)
