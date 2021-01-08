#ac
import copy

def dfs(hang,lie):
    global step,s
    if step == (r-1)*(c-1):
        if len(ans) == 0:
            ans.append(copy.deepcopy(s))
        else:
            if s < ans[0]:
                ans[0] = copy.deepcopy(s)
        return
    if len(ans) == 1:
        if s > ans[0]:
            return
    for i in [2,-2]:
        if 0<lie+i<c:
            for j in [1,-1]:
                if 0<hang+j<r:
                    if mark[hang+j][lie+i] == 0:
                        step += 1
                        mark[hang+j][lie+i] = step
                        s += trans[hang+j]
                        s += str(lie+i)
                        dfs(hang+j,lie+i)
                        mark[hang+j][lie+i] = 0
                        s = s[:-2]
                        step -= 1
    for i in [2,-2]:
        if 0<hang+i<r:
            for j in [1,-1]:
                if 0<lie+j<c:
                    if mark[hang+i][lie+j] == 0:
                        step += 1
                        mark[hang+i][lie+j] = step
                        s += trans[hang+i]
                        s += str(lie+j)
                        dfs(hang+i,lie+j)
                        mark[hang+i][lie+j] = 0
                        s = s[:-2]
                        step -= 1

trans = dict()
trans[1] = 'A'
trans[2] = 'B'
trans[3] = 'C'
trans[4] = 'D'
trans[5] = 'E'
trans[6] = 'F'
trans[7] = 'G'
trans[8] = 'H'
trans[9] = 'I'
trans[10] = 'J'
trans[11] = 'K'
trans[12] = 'L'
trans[13] = 'M'
trans[14] = 'N'
trans[15] = 'O'
trans[16] = 'P'
trans[17] = 'Q'
trans[18] = 'R'
trans[19] = 'S'
trans[20] = 'T'
trans[21] = 'U'
trans[22] = 'V'
trans[23] = 'W'
trans[24] = 'X'
trans[25] = 'Y'
trans[26] = 'Z'
n = int(input())
count = 0
while count < n:
    if count > 0:
        print()
    line = input().strip().split()
    c = int(line[0]) + 1   #列 用1234表示
    r = int(line[1]) + 1   #行 用ABCD表示
    mark1 = []
    mark = []
    for i in range(r):
        for j in range(c):
            mark1.append(0)
        mark.append(copy.deepcopy(mark1))
    s = 'A1'
    step = 1
    mark[1][1] = 1
    ans = []
    dfs(1,1)
    count += 1
    print('Scenario #{}:'.format(count))
    if len(ans) == 0:
        print('impossible')
    else:
        ans = sorted(ans)
        print(ans[0])
