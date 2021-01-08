#dfs
import copy

def dfs(x,y):
    global step,minstep,final_ans
    if x == 4 and y == 4:
        if step < minstep:
            minstep = step
            final_ans = copy.deepcopy(ans)
        return

    if step > minstep:
        return

    for i in range(4):
        if -1<x+direction[i][0]<5 and -1<y+direction[i][1]<5 and visited[x+direction[i][0]][y+direction[i][1]]==0 and maze[x+direction[i][0]][y+direction[i][1]] == '0':
            visited[x+direction[i][0]][y+direction[i][1]] = 1
            ans.append((x+direction[i][0],y+direction[i][1]))
            step += 1
            dfs(x+direction[i][0],y+direction[i][1])
            step -= 1
            visited[x+direction[i][0]][y+direction[i][1]] = 0
            del ans[-1]
    return

maze = []
for i in range(5):
    line = input().strip().split()
    maze.append(copy.deepcopy(line))
#读入maze
visited = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
ans = [(0,0)]
minstep = 1000000000000
step = 1
direction = [[1,0],[-1,0],[0,1],[0,-1]]
dfs(0,0)
for i in final_ans:
    print(i)
