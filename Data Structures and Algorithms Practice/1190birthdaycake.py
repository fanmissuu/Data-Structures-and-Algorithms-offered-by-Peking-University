#ac
def maxVforNRH(n,r,h):     #求在n层蛋糕，底层最大半径r，最高高度h的情况下，能凑出来的最大体积
    v = 0
    for i in range(n):
        v += (r-i) * (r-i) * (h-i)
    return v

def dfs(v,n,r,h):      #用n层去凑体积v,最底层半径最大为r,高度最大为h
    global minArea,area
    if n == 0:
        if v != 0:
            return
        minArea = min(area, minArea)
        return
    if v <= 0:
        return
    if minV[n] > v:
        return
    if area + minA[n] > minArea:
        return
    if r<n or h<n:
        return
    if maxVforNRH(n,r,h) < v:
        return
    for rr in range(r,n-1,-1):
        if n == M:
            area = rr * rr
        for hh in range(h,n-1,-1):
            area += 2 * rr * hh
            dfs(v-rr*rr*hh,n-1,rr-1,hh-1)
            area -= 2 * rr * hh
    return


N = int(input())
M = int(input())
minV = []
minA = []
for i in range(M+1):
    minA.append(0)
    minV.append(0)
for i in range(1,M+1):
    minV[i] = minV[i-1] + i**3
    minA[i] = minA[i-1] + 2*i*i
if minV[M] > N:
    print(0)
else:
    H = int((N - minV[M-1]) / (M*M))
    R = int(((N - minV[M-1]) / M) ** 0.5)
    area = 0
    minArea = 1000000000000000
    dfs(N,M,R,H)
    if minArea == 1000000000000000:
        print(0)
    else:
        print(minArea)
