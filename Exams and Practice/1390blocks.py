#对 但超时
def click_box(start,end,ex_len):
    if res[start][end][ex_len] != -1:
        return res[start][end][ex_len]
    if start == end:
        res[start][end][ex_len] = (segment[end][-1] + ex_len) ** 2
        return res[start][end][ex_len]
    result = (segment[end][-1] + ex_len) ** 2 + click_box(start,end-1,0)
    for p in range(start,end):
        if segment[p][0] != segment[end][0]:
            continue
        temp = click_box(start,p,segment[end][-1]+ex_len) + click_box(p+1,end-1,0)
        if temp > result:
            result = temp
    res[start][end][ex_len] = result
    return res[start][end][ex_len]

N = int(input())
count = 0
while count < N:
    n = int(input())
    count += 1
    boxes1 = input().strip().split()
    boxes = []
    for i in boxes1:
        boxes.append(int(i))
    #读入N和boxes
    segment = []
    count_len = 1
    for i in range(n-1):
        if boxes[i] == boxes[i+1]:
            count_len += 1
        else:
            segment.append([boxes[i],count_len])
            count_len = 1
    if len(segment) == 0:
        segment.append([boxes[0],1])
    else:
        if boxes[-1] == segment[-1][0]:
            segment[-1][-1] += 1
        else:
            segment.append([boxes[-1],1])
    #读入blocks数目  end=blocks数目-1     segment = [(color数字,len)……] end为segment的下标
    res = []
    for i1 in range(n):
        res.append([])
        for i2 in range(n):
            res[i1].append([])
            for i3 in range(n):
                res[i1][i2].append(-1)
    print('Case {}: {}'.format(count,click_box(0,len(segment)-1,0)))
