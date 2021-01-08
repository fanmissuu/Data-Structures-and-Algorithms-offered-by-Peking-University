#ac  辗转相除法   a,b的最大公约数 == a-b,b的最大公约数
def common(a,b):
    if a % b == 0:
        return b
    elif b == 1:
        return 1
    else:
        return common(b,a%b)
while True:
    try:
        line = input()
    except EOFError:
        break
    line = line.strip().split()
    x = int(line[0])
    y = int(line[1])
    if x > y:
        a = x
        b = y
    else:
        a = y
        b = x
    print(common(a,b))
