#ac
def available(r,c):  #判断某个皇后是否与已有皇后冲突
    for i in range(1,r):
        if c == queen[i]:
            return False
        if r-i == abs(c-queen[i]):
            return False
    return True

def dfs(h):
    if h > 8:
        s = ''
        for i in range(1,9):
            s += str(queen[i])
        ans.append(int(s))
        return
    for i in range(1,9):
        if h == 1:
            queen[h] = i
            dfs(h+1)
        else:
            if available(h,i):
                queen[h] = i
                dfs(h+1)
    return

queen = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
ans = []

n = int(input())
count = 0
dfs(1)
ans = sorted(ans)
while count < n:
    b = int(input())
    print(ans[b-1])
    count += 1
