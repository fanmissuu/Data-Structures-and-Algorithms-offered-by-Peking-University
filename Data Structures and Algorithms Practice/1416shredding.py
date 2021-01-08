#ac
import copy

def dfs(string,cursum):
    global maxx,ischeck,path
    if string == '':
        if cursum == maxx:
            path = copy.deepcopy(p)
            ischeck = False
        if cursum > maxx:
            maxx = cursum
            path = copy.deepcopy(p)
            ischeck = True
        return
    for i in range(len(string)):
        startnum = int(string[:i+1])
        if startnum + cursum > target:
            continue
        cursum += startnum
        p.append(i+1)
        dfs(string[i+1:],cursum)
        cursum -= startnum
        del p[-1]


while True:
    line = input().strip().split()
    if int(line[0]) == 0 and int(line[1]) == 0:
        break
    if line[0] == line[1]:           #target == num
        print("{} {}".format(line[0],line[1]))
        continue
    target = int(line[0])
    minsum = 0
    for i in line[1]:
        minsum += int(i)
    if minsum > target:      #error
        print('error')
        continue
    num = line[1]
    maxx = 0
    p = []
    dfs(num,0)
    startpos = 0
    if not ischeck:
        print('rejected')
    else:
        print(maxx,end=' ')
        for j in range(len(path)):
            if j == len(path)-1:
                print(num[startpos:startpos+path[j]])
            else:
                print(num[startpos:startpos+path[j]],end = ' ')
                startpos += path[j]
