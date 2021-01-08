
def fun(n,i):
    if n == 0:
        return 1
    elif n%2 == 1 and i == 0:
        return 0
    elif n%2 == 0 and i == 1:
        return 0
    elif n == 1 and i == 1:
        return 1
    elif n == 2 and i == 0:
        return 3

    if n > 2 and i == 0:
        return fun(n-2,0) + 2 * fun(n-1,1)
    if n > 2 and i == 1:
        return fun(n-1,0) + fun(n-2,1)

while True:
    n = int(input())
    if n == -1:
        break
    num = fun(n,0)
    print(num)
