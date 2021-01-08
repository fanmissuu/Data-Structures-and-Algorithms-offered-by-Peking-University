#ac   贪心+枚举
count = 0
while True:
    n = int(input())
    if n == 0:
        break
    if count != 0:
        print()
    h = int(input()) * 12
    fi = input().strip().split()
    di = input().strip().split()
    ti = input().strip().split()
    #读入数据
    ANS = -1    #注意：此处需要初始化为-1，才能保证在ans=0时也有输出
    for i in range(n):
        ans = 0
        nowfish = []
        each = []
        effi_h = h
        for j in range(n):
            each.append(0)    #each必须初始化为size与n一致，而不是与枚举的size一致，才能保证输出形式为‘x, 0, 0, 0, ……’，不然输出可能为‘x’就结束了。
        for j in range(i+1):
            nowfish.append(0)
            nowfish[j] = int(fi[j])
            if j > 0 :
                effi_h -= int(ti[j-1])
        while effi_h > 0:
            ind = 0
            nowbest = nowfish[ind]
            for j in range(1,i+1):
                if nowfish[j] > nowbest:
                    nowbest = nowfish[j]
                    ind = j
            if nowbest <= 0:
                each[0] += effi_h * 5
                break
            else:
                each[ind] += 5
                ans += nowbest
            if nowfish[ind] > int(di[ind]):
                nowfish[ind] -= int(di[ind])
            else:
                nowfish[ind] = 0
            effi_h -= 1
        if ans > ANS:
            ANS = ans
            lake = each
    for j in range(len(lake)):
        if j == len(lake) - 1:
            print(lake[j])
        else:
            print('{}, '.format(lake[j]),end = '')
    print('Number of fish expected: {}'.format(ANS))
    count += 1

count = 0
while True:
    n = int(input())
    if n == 0:
        break
    if count != 0:
        print()
    h = int(input()) * 12
    fi = input().strip().split()
    di = input().strip().split()
    ti = input().strip().split()
    #读入数据
    ANS = -1
    for i in range(n):
        ans = 0
        nowfish = []
        each = []
        effi_h = h
        for j in range(n):
            each.append(0)
        for j in range(i+1):
            nowfish.append(0)
            nowfish[j] = int(fi[j])
            if j > 0 :
                effi_h -= int(ti[j-1])
        while effi_h > 0:
            ind = 0
            nowbest = nowfish[ind]
            for j in range(1,i+1):
                if nowfish[j] > nowbest:
                    nowbest = nowfish[j]
                    ind = j
            if nowbest <= 0:
                each[0] += effi_h * 5
                break
            else:
                each[ind] += 5
                ans += nowbest
            if nowfish[ind] > int(di[ind]):
                nowfish[ind] -= int(di[ind])
            else:
                nowfish[ind] = 0
            effi_h -= 1
        if ans > ANS:
            ANS = ans
            lake = each
    for j in range(len(lake)):
        if j == len(lake) - 1:
            print(lake[j])
        else:
            print('{}, '.format(lake[j]),end = '')
    print('Number of fish expected: {}'.format(ANS))
    count += 1
#https://blog.csdn.net/hdd871532887/article/details/50449057?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight
