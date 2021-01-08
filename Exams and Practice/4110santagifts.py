line = input().strip().split()
N = int(line[0])
W = int(line[1])
count = 0
candy = []
while count < N:
    line = input().strip().split()
    candy.append([int(line[0]),int(line[1]),round(int(line[0])/int(line[1]),3)])
    count += 1
tov = 0
tow = 0
candy = sorted(candy, reverse = True, key = lambda x:x[2])
for i in candy:
    if tow + i[1] <= W:
        tow += i[1]
        tov += i[0]
    else:
        tov += i[2] * (W - tow)
        tow = W
        break
print('{:.1f}'.format(tov))
