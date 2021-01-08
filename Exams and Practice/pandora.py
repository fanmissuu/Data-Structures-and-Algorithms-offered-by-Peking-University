#poj无此题  答案对。
import copy

d = [[1,0],[-1,0],[0,1],[0,-1]]
nextSides = [[4,5,3,1],[4,5,0,2],[4,5,1,3],[4,5,2,0],[2,0,3,1],[2,0,3,1]]  #每个面的udlr邻面
def dfs(side,i,j):
    global roomNum,roomArea
    if a[side][i][j] != '0':
        return
    roomArea += 1
    a[side][i][j] = roomNum
    for di in d:
        newI = i + di[0]
        newJ = j + di[1]
        newSide = side
        if side != 4 and side != 5:    #四周面左右移
            if newJ < 0:
                newJ = k-1
                newSide = nextSides[side][2]
            if newJ >= k:
                newJ = 0
                newSide = nextSides[side][3]
        if side != 1 and side != 3:      # 前后上下面上下移
            if side == 2 and (newI < 0 or newI >= k):
                newJ = k - 1 - newJ  #面2因为是反面，所以需要先翻转列坐标; 本来在2面，现不在2面了。
            if newI < 0:
                newSide = nextSides[side][0]
                if side == 2 or side == 4:
                    newI = 0
                else:
                    newI = k - 1
            if newI >= k:
                newSide = nextSides[side][1]
                if side == 0 or side == 5:
                    newI = k - 1
                else:
                    newI = 0
            if newSide == 2 and side != 2:   #原来不在2面，现在在2面,列坐标再反转回去
                newJ = k - 1 - newJ
        if side != 0 and side != 2:
            if side == 4:    #上面左右移
                if newJ < 0:
                    newSide = nextSides[side][2]
                    newJ = newI
                    newI = 0
                if newJ >= k:
                    newSide = nextSides[side][3]
                    newJ = k - 1 - newI
                    newI = 0
            if side == 5:    #下面左右移
                if newJ < 0:
                    newSide = nextSides[side][2]
                    newJ = newI
                    newI = k - 1
                if newJ >= k:
                    newSide = nextSides[side][3]
                    newJ = k - 1 - newI
                    newI = k - 1
            if side == 1:   #右面上下移
                if newI < 0:
                    newSide = nextSides[side][0]
                    newI = k - 1 - newJ
                    newJ = k - 1
                if newI >= k:
                    newSide = nextSides[side][1]
                    newI = k - 1 - newJ
                    newJ = k - 1
            if side == 3:  #左面上下移
                if newI < 0:
                    newSide = nextSides[side][0]
                    newI = newJ
                    newJ = 0
                if newI >= k:
                    newSide = nextSides[side][1]
                    newI = newJ
                    newJ = 0
        if a[newSide][newI][newJ] == '0':
            dfs(newSide,newI,newJ)

T = int(input())
for t in range(T):
    k = int(input())
    a = []
    for eve_side in range(6):
        a1 = []
        for eve_line in range(k):
            line = input().strip().split()
            a1.append(copy.deepcopy(line))
        a.append(copy.deepcopy(a1))
    #读入每组数据
    roomNum = 1   #本应是0  但为了与题目中的墙1做区分 从2开始标注。
    maxroomArea = 0

    for side in range(6):
        for i in range(k):
            for j in range(k):
                if a[side][i][j] == '0':    #注意是字符
                    roomNum += 1
                    roomArea = 0
                    dfs(side,i,j)
                    maxroomArea = max(maxroomArea, roomArea)

    print('{} {}'.format(roomNum-1,maxroomArea))
