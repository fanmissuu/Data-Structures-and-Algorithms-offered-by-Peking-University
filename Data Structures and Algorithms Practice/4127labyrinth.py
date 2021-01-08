#bfs
import copy
direction = [[1,0],[-1,0],[0,1],[0,-1]]
maze = []
visited = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(5):
    line = input().strip().split()
    maze.append(copy.deepcopy(line))
#读入maze
s = [[0,0]]
path_dict = {}
path_dict[(0,0)] = (-1,-1)
while len(s) != 0:
    top = s[0]
    if top == [4,4]:
        ans = [(4,4)]
        nex_pos = path_dict[(4,4)]
        while not nex_pos[0] == -1:
            ans.append(nex_pos)
            nex_pos = path_dict[nex_pos]
        for j in range(len(ans)-1,-1,-1):
            print(ans[j])
        break
    for i in range(4):
        if -1<top[0]+direction[i][0]<5 and -1<top[1]+direction[i][1]<5 and visited[top[0]+direction[i][0]][top[1]+direction[i][1]]==0 and maze[top[0]+direction[i][0]][top[1]+direction[i][1]] == '0':
            s.append([top[0]+direction[i][0],top[1]+direction[i][1]])
            visited[top[0]+direction[i][0]][top[1]+direction[i][1]] = 1
            path_dict[(top[0]+direction[i][0],top[1]+direction[i][1])] = (top[0],top[1])
    del s[0]
