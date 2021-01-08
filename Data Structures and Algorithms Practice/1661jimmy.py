#meng检查没发现错误但未ac
def MinTime(I,flag):
    y = data_set[I][2]
    if I == len(data_set) -1:
        if y > int(line[3]):
            return 'INFINITE'
        else:
            return y
    if flag:
        x = int(data_set[I][0])
    else:
        x = int(data_set[I][1])
    flag1 = False
    for i in range(I+1,len(data_set)):
        if int(data_set[i][0]) <= x and int(data_set[i][1]) >= x:
            flag1 = True
            break
    if not flag1:
        if y > int(line[3]):
            return 'INFINITE'
        else:
            return y
    if flag1:
        if y - data_set[i][2] > int(line[3]):
            return 'INFINITE'
        else:
            nLeftTime = y - data_set[i][2] + x - int(data_set[i][0])
            nRightTime = y - data_set[i][2] + int(data_set[i][1]) - x
            if leftMinTime[i] == -1:
                leftMinTime[i] = MinTime(i,True)      #leftMinTime[i]和rightMinTime[i]的意义
            if rightMinTime[i] == -1:
                rightMinTime[i] = MinTime(i,False)
            nLeftTime += leftMinTime[i]
            nRightTime += rightMinTime[i]
            if nLeftTime <= nRightTime:
                return nLeftTime
            return nRightTime



n = int(input())
count = 0
while count < n:
    line = input().strip().split()
    count += 1
    count1 = 0
    data_set = [[line[1],line[1],line[2]]]
    while count1 < int(line[0]):
        data_set.append(input().strip().split())
        count1 += 1
    for i in data_set:
        i[2] = int(i[2])
    data_set = sorted(data_set, reverse=True, key=lambda x:x[2])
    #data_set读入每一组的所有platform(包括起始点)，并按h进行排序
    leftMinTime = []
    rightMinTime = []
    for i in range(int(line[0])+1):
        leftMinTime.append(-1)
        rightMinTime.append(-1)
    print(MinTime(0,True))
