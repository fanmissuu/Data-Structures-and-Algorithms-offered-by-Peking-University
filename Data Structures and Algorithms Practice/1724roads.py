#ac
import copy

def dfs(s):
    global totalLen,totalCost,minLen
    if s == N:
        minLen = min(minLen,totalLen)
        return

    if cityMap[s] != []:
        for j in cityMap[s]:
            d = j[0]
            if visited[d] == 0:
                cost = totalCost + j[2]
                if cost > K:
                    cost = totalCost - j[2]
                    continue
                if totalLen + j[1] >= minLen or totalLen + j[1] >= minL[d][cost]:
                    continue
                totalLen += j[1]
                totalCost += j[2]
                minL[d][cost] = totalLen
                visited[d] = 1
                dfs(d)
                #minL[d][cost] = 100000000000  加上这一行就会超时
                visited[d] = 0
                totalLen -= j[1]
                totalCost -= j[2]
        return

K = int(input())
N = int(input())
R = int(input())
count = 0
roads = []
while count < R:
    road = []
    line = input().strip().split()
    for i in line:
        road.append(int(i))
    roads.append(copy.deepcopy(road))
    count += 1
    #读入roads
cityMap = []
for i in range(N+1):
    cityMap.append([])
for i in roads:
    if i[0] != i[1]:
        cityMap[i[0]].append([i[1],i[2],i[3]])
#生成cityMap N+1行   index为起点城市
minL = []
for i in range(N+1):
    minL1 = []
    for j in range(K+1):
        minL1.append(100000000000)
    minL.append(copy.deepcopy(minL1))
#生成minL N+1行 K+1列  表示走到城市i，花费为j时的最优路径长度。
visited = []
for i in range(N+1):
    visited.append(0)
totalLen = 0
totalCost = 0
minLen = 100000000000
visited[1] = 1
dfs(1)
if minLen < 100000000000:
    print(minLen)
else:
    print('-1')
