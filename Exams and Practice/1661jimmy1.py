#meng检查没发现错误但未ac
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
    for i in range(len(data_set)):
        leftMinTime.append(-1)
        rightMinTime.append(-1)
    if data_set[-1][2] > int(line[3]):
        leftMinTime[-1] = 'INFINITE'
        rightMinTime[-1] = 'INFINITE'
    else:
        leftMinTime[-1] = data_set[-1][2]
        rightMinTime[-1] = data_set[-1][2]
    for i in range(len(data_set)-2,-1,-1):
        flag1 = False
        for j in range(i+1,len(data_set)):
            if int(data_set[i][0]) >= int(data_set[j][0]) and int(data_set[i][0]) <= int(data_set[j][1]):
                flag1 = True
                break
        if not flag1:
            if data_set[i][2] > int(line[3]):
                leftMinTime[i] = 'INFINITE'
            else:
                leftMinTime[i] = data_set[i][2]
        else:
            y = data_set[i][2] - data_set[j][2]
            if y > int(line[3]):
                leftMinTime[i] = 'INFINITE'
            else:
                leftMinTime[i] = y + min(leftMinTime[j]+int(data_set[i][0])-int(data_set[j][0]),rightMinTime[j]+int(data_set[j][1])-int(data_set[i][0]))
        flag2 = False
        for j in range(i+1,len(data_set)):
            if int(data_set[i][1]) >= int(data_set[j][0]) and int(data_set[i][1]) <= int(data_set[j][1]):
                flag2 = True
                break
        if not flag2:
            if data_set[i][2] > int(line[3]):
                rightMinTime[i] = 'INFINITE'
            else:
                rightMinTime[i] = data_set[i][2]
        else:
            y = data_set[i][2] - data_set[j][2]
            if y > int(line[3]):
                rightMinTime[i] = 'INFINITE'
            else:
                rightMinTime[i] = y + min(leftMinTime[j]+int(data_set[i][1])-int(data_set[j][0]),rightMinTime[j]+int(data_set[j][1])-int(data_set[i][1]))
    print(leftMinTime[0])
