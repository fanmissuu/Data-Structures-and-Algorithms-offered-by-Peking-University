# 完全独立完成。
#https://blog.csdn.net/weixin_30700977/article/details/96546367?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight
#https://blog.csdn.net/Rage_/article/details/58706774?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.edu_weight
#以上两个为网上普遍做法 比我的方法速度快。我枚举的是总桃子数，网上的方法是枚举第n只猴子拿走的数目。
def check(X):
    global N
    for i in range(N):
        if X-1 > 0 and (X-1) % N == 0:
            X = X - 1 - (X - 1)/N
        else:
            return False
    return True

while True:
    N = int(input())
    if N == 0:
        break
    ans = 2 * N
    while not check(ans):
        ans += 1
    print(ans)
