line = input().strip().split()
N = int(line[0])
K = int(line[1])
visited = []
for i in range(100001):
    visited.append(0)
s = [[N,0]]
visited[N] = 1
while len(s) != 0:
    now_pos = s[0][0]
    step = s[0][1]
    if now_pos == K:
        time = s[0][1]
        break
    else:
        if now_pos-1 >= 0 and visited[now_pos-1] == 0:
            s.append([now_pos-1,step+1])
            visited[now_pos-1] = 1
        if now_pos+1 <= 100000 and visited[now_pos+1] == 0:
            s.append([now_pos+1,step+1])
            visited[now_pos+1] = 1
        if now_pos*2 <= 100000 and visited[now_pos*2] == 0:
            s.append([now_pos*2,step+1])
            visited[now_pos*2] = 1
    del s[0]
print(time)
