#runtime error   但是测试数据都对
import copy

def solve(a):
    ans = 1
    now = a[0][1]
    if len(a) == 1:
        return 1
    else:
        for i in range(1,len(a)):
            if a[i][0] <= now:
                now = min(now,a[i][1])
            else:
                ans += 1
                now = a[i][1]
        return ans


count = 0
while True:
    line = input().strip().split()
    if line == ['0','0']:
        break
    count += 1
    flag = True
    n = int(line[0])
    d = int(line[1])
    left_right = []
    for i in range(n):
        each_island = input().strip().split()
        if abs(int(each_island[1])) > abs(d) or d < 0:
            flag = False
        else:
            side = round(pow(d ** 2 - int(each_island[1]) ** 2, 0.5),5)
            left = int(each_island[0]) - side
            right = int(each_island[0]) + side
            left_right.append([copy.deepcopy(left),copy.deepcopy(right)])
    if not flag:
        print('Case {}: -1'.format(count))
        continue
    left_right = sorted(left_right, key=lambda x:x[0])
    print('Case {}: {}'.format(count,solve(left_right)))
