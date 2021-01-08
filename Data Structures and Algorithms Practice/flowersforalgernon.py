#完全独立完成
import copy

def check(x,y):
    global R,C
    if 0 <= x < R and 0 <= y < C:
        return True
    else:
        return False

T = int(input())
direction = [[0,1],[0,-1],[1,0],[-1,0]]
for eve_group in range(T):
    RC = input().strip().split()
    R = int(RC[0])
    C = int(RC[1])
    maze = []
    for eve_line in range(R):
        maze.append(input().strip())
    #读入每组数据

    visited1 = []
    visited = []
    s = []
    for col in range(C):
        visited1.append(0)
    for row in range(R):
        visited.append(copy.deepcopy(visited1))
    for row in range(R):
        for col in range(C):
            if maze[row][col] == 'S':
                s.append([row,col,0])
                visited[row][col] = 1
    flag = 0
    while len(s) != 0:
        now_pos = s[0]
        now_x = now_pos[0]
        now_y = now_pos[1]
        step = now_pos[2]
        if maze[now_x][now_y] == 'E':
            ans = step
            flag = 1
            break
        else:
            for i in direction:
                if check(now_x+i[0],now_y+i[1]):
                    if visited[now_x+i[0]][now_y+i[1]] == 0:
                        if maze[now_x+i[0]][now_y+i[1]] == '.' or maze[now_x+i[0]][now_y+i[1]] == 'E':
                            s.append([now_x+i[0],now_y+i[1],step+1])
                            visited[now_x+i[0]][now_y+i[1]] = 1
            del s[0]
    else:
        print('oop!')
    if flag == 1:
        print(ans)
