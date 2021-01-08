import copy

l = []
while True:
    a = input().strip()
    if a == '#':
        l.append(copy.deepcopy(a))
        break
    else:
        l.append(copy.deepcopy(a))


def paint(n1,n2):
    global finish
    finish = True
    for i in range(n1,n2):
        if not l[i].startswith('f'):
            finish = False
            break
    if finish == True:
        return
    file = []
    for i in range(n1,n2):
        if l[i].startswith('f'):
            file.append(l[i])
        elif l[i].startswith('d'):
            paint(i,n2)
