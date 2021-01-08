import copy

to =[[0,1],[1,0],[0,-1],[-1,0]]
minstep = 100000
def search(now_y,now_x,end_y,end_x,step,f):
    global minstep
    if step >= minstep:
        return
    if now_x == end_x and now_y == end_y:
        if minstep > step:
            minstep = step
        return
    for ii in range(4):
        y = now_y + to[ii][1]
        x = now_x + to[ii][0]
        if (0 <= x <= w+1 and 0 <= y <= h+1 and mark[y][x] == 'False' and board[y][x] == ' ') or (0 <= x <= w+1 and 0 <= y <= h+1 and x == end_x and y == end_y and board[y][x] == 'X'):
            mark[y][x] = 'True'
            if f == ii:
                search(y,x,end_y,end_x,step,ii)
            else:
                search(y,x,end_y,end_x,step+1,ii)
            mark[y][x] = 'False'
    return

count = 0
while True:
    wh = input()
    if wh == '0 0':
        break
    w = int(wh.strip().split()[0])
    h = int(wh.strip().split()[1])
    count += 1
    if count == 1:
        print('Board #{}:'.format(count))
    else:
        print()
        print('Board #{}:'.format(count))

    board1 = []
    for i in range(h):
        board1.append(input())
    a = []
    for i in range(w+2):
        a.append(' ')
    board = [copy.deepcopy(a)]
    for i in range(h):
        for j in range(w):
            a[j+1] =board1[i][j]
        board.append(copy.deepcopy(a))
    board.append(copy.deepcopy(board[0]))
    #读入游戏板 board为四周为了一圈的矩阵

    pair = 0
    while True:
        target = input()
        if target == '0 0 0 0':
            break
        else:
            pair += 1
            target = target.strip().split()

            mark = []
            mark1 = []
            for i in range(h+2):
                for j in range(w+2):
                    mark1.append('False')
                mark.append(copy.deepcopy(mark1))
                mark1 = []

            search(int(target[1]),int(target[0]),int(target[3]),int(target[2]),0,-1)
            if minstep <100000:
                print('Pair {}: {} segments.'.format(pair,minstep))
                minstep = 100000
            else:
                print('Pair {}: impossible.'.format(pair))
                minstep = 100000
