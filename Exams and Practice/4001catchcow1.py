#compile error
import copy
def dfs(N):
    global step,ans
    if step >= ans:
        return
    if N == K:
        if step < ans:
            ans = step
        return
    else:
        if N-1 >= 0 and visited[N-1] == 0:
            visited[N-1] = 1
            step += 1
            dfs(N-1)
            visited[N-1] = 0
            step -= 1
        if N+1 <= 100000 and visited[N+1] == 0:
            visited[N+1] = 1
            step += 1
            dfs(N+1)
            visited[N+1] = 0
            step -= 1
        if N*2 <= 100000 and visited[N*2] == 0:
            visited[N*2] = 1
            step += 1
            dfs(N*2)
            visited[N*2] = 0
            step -= 1
        return
line = input().strip().split()
N = int(line[0])
K = int(line[1])
visited = []
for i in range(100100):
    visited.append(0)
step = 0
ans = 100000000
visited[N] = 1
dfs(N)
print(ans)
