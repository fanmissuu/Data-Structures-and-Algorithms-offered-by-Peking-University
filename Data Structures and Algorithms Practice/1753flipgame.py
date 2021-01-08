#ac
import copy
def judge(x,y):
    if -1 < x < 4 and -1 < y < 4:
        return True
    else:
        return False

def initialize():
    for i in range(4):
        for j in range(4):
            val = 0
            val += 1 << (i * 4 + j)
            for k in direction:
                nex_x = i + k[0]
                nex_y = j + k[1]
                if judge(nex_x,nex_y):
                    val += 1 << (nex_x * 4 + nex_y)
            pos[i * 4 + j] = copy.deepcopy(val)


direction = [[1,0],[-1,0],[0,1],[0,-1]]
pos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
value = 0
for i in range(4):
    line = input().strip()
    for j in range(4):
        if line[j] == 'w':
            value += 1 << (i * 4 + j)
initialize()
s = [[value,0]]
visited = []
for v in range(65536):         #2^16-1 = 65535  65535要能取到
    visited.append(0)
visited[value] = 1
while len(s) != 0:
    if s[0][0] == 0 or s[0][0] == (1 << 16) - 1:
        ans = s[0][1]
        break
    for h in range(16):
        next = s[0][0] ^ pos[h]
        if visited[next] == 0:
            s.append([copy.deepcopy(next),s[0][1]+1])
            visited[next] = 1
    del s[0]
else:
    ans ='Impossible'
print(ans)


#https://dreamer.blue/blog/post/2016/07/25/poj-1753.dream  讲得很清楚
