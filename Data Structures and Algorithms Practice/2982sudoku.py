#ac
import copy

def getboardNum(r,c):
    rr = r//3
    cc = c//3
    return rr*3+cc

def setallFlags(i,j,num,f):
    rowFlags[i][num] = f
    colFlags[j][num] = f
    blockFlags[getboardNum(i,j)][num] = f

def isok(i,j,num):
    if rowFlags[i][num] == 0 and colFlags[j][num] == 0 and blockFlags[getboardNum(i,j)][num] == 0:
        return True
    else:
        return False

def dfs(nn):
    if nn < 0:
        return True
    r = blankpos[nn][0]
    c = blankpos[nn][1]
    for i in range(1,10):
        if isok(r,c,i):
            board[r][c] = i
            setallFlags(r,c,i,1)
            if dfs(nn-1):
                return True
            setallFlags(r,c,i,0)
    return False


group = int(input())
count = 0
while count < group:
    rowFlags = []
    colFlags = []
    blockFlags = []
    rowFlags1 = []
    colFlags1 = []
    blockFlags1 = []
    for i in range(10):
        rowFlags1.append(0)
        colFlags1.append(0)
        blockFlags1.append(0)
    for i in range(9):
        rowFlags.append(copy.deepcopy(rowFlags1))
        colFlags.append(copy.deepcopy(colFlags1))
        blockFlags.append(copy.deepcopy(blockFlags1))
    #设置rowFlags,colFlags,blockFlags矩阵 9行10列全为0
    count += 1
    board = []
    for i in range(9):
        board1 = []
        board1 = ' '.join(input()).split()
        for j in range(9):
            board1[j] = int(board1[j])
        board.append(copy.deepcopy(board1))

    #读入数独板
    blankpos = []
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                setallFlags(i,j,board[i][j],1)
            else:
                blankpos.append((i,j))
    #根据数独板，设置好rowFlags,colFlags,blockFlags和blankpos
    if dfs(len(blankpos)-1):
        s = ''
        for i in board:
            for j in i:
                s += str(j)
            print(s)
            s = ''
