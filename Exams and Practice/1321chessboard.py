#ac
import copy

def dfs(h):     #h为行数
    global already,total
    if k == already:
        total += 1
        return
    if h >= n:
        return
    for i in range(n):   #对于每一行，有n+1种可能性。n：放在n列中的某一列   1:此行不放，直接进入下一行dfs(h+1)
        if board[h][i] == '#' and res[i] == 0:          #(接上一行注释)所以dfs(h+1)和for的遍历循环在同一层次
            res[i] = 1
            already += 1
            dfs(h+1)
            res[i] = 0
            already -= 1
    dfs(h+1)
    return     #这个return写不写都一样  因为函数最后都要return


while True:
    line = input()
    if line == '-1 -1':
        break
    n = int(line[0])
    k = int(line[2])
    count = 0
    board = []
    while count < n:
        boardline = input().strip()
        board.append(copy.deepcopy(boardline))
        count += 1
    #读入数据
    res = []
    for i in range(n):
        res.append(0)
    #res记录每一列是否放过棋子
    already = 0
    total = 0
    dfs(0)
    print(total)
