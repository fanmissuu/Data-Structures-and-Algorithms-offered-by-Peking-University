#ac
import copy

def check(ans):
    s = 0
    now = 0
    for i in range(len(books)-1,-1,-1):
        if now + books[i] > ans:
            s += 1
            now = books[i]
        else:
            now += books[i]
    if now > 0:
        s += 1
    if s <= k:
        return True
    else:
        return False

def printit(bookk,person,ans,noww):
    sepa = False
    if bookk < 0:
        return
    if bookk == person - 1 or noww + books[bookk] > ans:   #不能放入当前堆
        sepa = True
        printit(bookk-1,person-1,ans,books[bookk])
    else:
        printit(bookk-1,person,ans,noww+books[bookk])
    if bookk > 0:
        print(' {}'.format(books[bookk]),end = '')
    else:
        print(books[bookk],end = '')
    if sepa:
        print(' /',end = '')

N = int(input())
for n in range(N):
    line = input().strip().split()
    m = int(line[0])   #几本书
    k = int(line[1])   #几个人
    books1 = input().strip().split()
    books = []
    l = 0
    r = 0
    for book in books1:
        books.append(int(book))
        r += int(book)
        if int(book) > l:
            l = copy.deepcopy(int(book))
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            r = mid - 1
        else:
            l = mid + 1
    printit(m-1,k-1,l,0)
    print()
