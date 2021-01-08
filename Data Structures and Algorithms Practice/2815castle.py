#自己 mn 觉得并没错  但wrong answer
import copy

def dfs(i,k):
    global roomNum,roomArea
    if color[i][k] != 0:
        return
    roomArea += 1
    color[i][k] = roomNum
    if rooms[i][k] == 1:
        dfs(i,k+1)
        dfs(i-1,k)
        dfs(i+1,k)
    if rooms[i][k] == 2:
        dfs(i,k+1)
        dfs(i,k-1)
        dfs(i+1,k)
    if rooms[i][k] == 3:
        dfs(i,k+1)
        dfs(i+1,k)
    if rooms[i][k] == 4:
        dfs(i,k-1)
        dfs(i+1,k)
        dfs(i-1,k)
    if rooms[i][k] == 5:
        dfs(i+1,k)
        dfs(i-1,k)
    if rooms[i][k] == 6:
        dfs(i,k-1)
        dfs(i+1,k)
    if rooms[i][k] == 7:
        dfs(i+1,k)
    if rooms[i][k] == 8:
        dfs(i,k+1)
        dfs(i,k-1)
        dfs(i-1,k)
    if rooms[i][k] == 9:
        dfs(i,k+1)
        dfs(i-1,k)
    if rooms[i][k] == 10:
        dfs(i,k-1)
        dfs(i,k+1)
    if rooms[i][k] == 11:
        dfs(i,k+1)
    if rooms[i][k] == 12:
        dfs(i,k-1)
        dfs(i-1,k)
    if rooms[i][k] == 13:
        dfs(i-1,k)
    if rooms[i][k] == 14:
        dfs(i,k-1)
    return

R = int(input())
C = int(input())
count = 0
rooms = []
while count < R:
    line = input().strip().split()
    eve_line = []
    for i in line:
        eve_line.append(int(i))
    rooms.append(copy.deepcopy(eve_line))
    count += 1
    #读入rooms
color1 = []
color = []
for i in range(C):
    color1.append(0)
for i in range(R):
    color.append(copy.deepcopy(color1))
#mark R行C列初始化为0

roomNum = 0
maxroomArea = 0
for i in range(R):
    for j in range(C):
        if color[i][j] == 0:
            roomNum += 1
            roomArea = 0
            dfs(i,j)
            maxroomArea = max(maxroomArea, roomArea)

print(roomNum)
print(maxroomArea)
