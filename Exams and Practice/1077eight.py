#答案是对的  但是运行的很慢很慢

import copy

initial = input().strip().split()
sigma = 0
for i in range(9):
    if initial[i] == 'x':
        x_pos = i
        continue
    if i == 0:
        continue
    else:
        for j in range(i):
            if initial[j] == 'x':
                continue
            if int(initial[j]) < int(initial[i]):
                sigma += 1
if sigma %2 == 1:
    print('unsolvable')
    exit()
step = 0
move = ''
res = [initial]
s = [[initial,x_pos,step,move]]
while len(s) != 0:
    now_str = s[0][0]
    if now_str == ['1','2','3','4','5','6','7','8','x']:
        break
    else:
        if s[0][1]-3 > -1:
            now_str1 = copy.deepcopy(now_str)
            now_str1[s[0][1]] = now_str1[s[0][1]-3]
            now_str1[s[0][1]-3] = 'x'
            if now_str1 not in res:
                s.append([copy.deepcopy(now_str1),s[0][1]-3,s[0][2]+1,s[0][3]+'u'])
                res.append(now_str1)
        if s[0][1]+3 < 9:
            now_str2 = copy.deepcopy(now_str)
            now_str2[s[0][1]] = now_str2[s[0][1]+3]
            now_str2[s[0][1]+3] = 'x'
            if now_str2 not in res:
                s.append([copy.deepcopy(now_str2),s[0][1]+3,s[0][2]+1,s[0][3]+'d'])
                res.append(now_str2)
        if s[0][1]-1 > -1 and s[0][1] != 0 and s[0][1] != 3 and s[0][1] != 6:
            now_str3 = copy.deepcopy(now_str)
            now_str3[s[0][1]] = now_str3[s[0][1]-1]
            now_str3[s[0][1]-1] = 'x'
            if now_str3 not in res:
                s.append([copy.deepcopy(now_str3),s[0][1]-1,s[0][2]+1,s[0][3]+'l'])
                res.append(now_str3)
        if s[0][1]+1 < 9 and s[0][1] != 2 and s[0][1] != 5 and s[0][1] != 8:
            now_str4 = copy.deepcopy(now_str)
            now_str4[s[0][1]] = now_str4[s[0][1]+1]
            now_str4[s[0][1]+1] = 'x'
            if now_str4 not in res:
                s.append([copy.deepcopy(now_str4),s[0][1]+1,s[0][2]+1,s[0][3]+'r'])
                res.append(now_str4)
        del s[0]
print(s[0][3])
