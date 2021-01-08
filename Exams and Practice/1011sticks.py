
def dfs(nUnused,nLeft):
    global nLastNo,nStartNo
    if nUnused == 0 and nLeft == 0:
        return True
    if nLeft == 0:
        nLeft = L
    if nLeft != L:
        nStartNo = nLastNo + 1
    else:
        nStartNo = 0
    for i in range(nStartNo,n):
        if used[i] == 0 and sticks[i] <= nLeft:
            if i > 0:
                if used[i-1] == 0 and sticks[i] == sticks[i-1]:
                    continue
            used[i] = 1
            nLastNo = i
            if dfs(nUnused-1,nLeft-sticks[i]):
                return True
            used[i] = 0
            if sticks[i] == nLeft or nLeft == L:
                return False
    return False


while True:
    n = int(input())
    if n == 0:
        break
    line = input().strip().split()
    sticks = []
    for i in line:
        sticks.append(int(i))
    sticks = sorted(sticks, reverse=True)
    totalLen = sum(sticks)
    #读入由大到小排好序的sticks和总长度L
    used = []
    for i in range(n):
        used.append(0)
    for L in range(sticks[0],totalLen//2+1):
        if totalLen % L != 0:
            continue
        if dfs(n,L):
            print(L)
            break
    else:
        print(totalLen)
