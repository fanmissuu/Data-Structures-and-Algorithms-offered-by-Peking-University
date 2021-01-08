find = False

visited[x][y] = False

def dfs(x, y):
    global find
    if x == x1 and y == y1:
        find = True
        return

    if find == True:
        return

    for option in options:
        if not option satisfies the condition:
            continue
        if visited[x][y+1] == True:
            continue
         # Suppose the current option is going up
         visited[x][y+1] = True
         dfs(x, y + 1)
         if find == True:
             return
         visited[x][y+1] = False
    return


#line11,12 和line22,23是相同的意思 两组中保留一组即可




void dfs()//参数用来表示状态
{
    if(到达终点状态)
    {
        ...//根据题意添加
        return;
    }
    if(越界或者是不合法状态)
        return;
    if(特殊状态)//剪枝
        return ;
    for(扩展方式)
    {
        if(扩展方式所达到状态合法)
        {
            修改操作;//根据题意来添加
            标记；
            dfs（）；
            (还原标记)；
            //是否还原标记根据题意
            //如果加上（还原标记）就是 回溯法
        }

    }
}  
