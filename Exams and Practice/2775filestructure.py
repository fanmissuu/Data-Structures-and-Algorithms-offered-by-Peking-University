import copy

l = []
while True:
    a = input().strip()
    if a == '#':
        l.append(copy.deepcopy(a))
        break
    else:
        l.append(copy.deepcopy(a))

count = 1
file = []
flag = True
flag1 = True
while flag1:
    if count == 1:
        print('DATA SET {}:'.format(count))
        print('ROOT')
    else:
        print()
        print('DATA SET {}:'.format(count))
        print('ROOT')
        flag = True
    while flag:
        if l[0] == '*':
            file = sorted(file)
            for j in file:
                print(j)
            file = []
            count += 1
            flag = False
            l.remove(l[0])
            continue
        if l[0].startswith('f'):
            file.append(l[0])
            l.remove(l[0])
            continue
        if l[0].startswith('d'):
            print('|     {}'.format(l[0]))
            l.remove(l[0])

        count1 = 0
        while True:
            if count1 == 2:
                break
            if count1 == 1:
                if l[0].startswith('d'):
                    print('|     {}'.format(l[0]))
                    count1 = 0
                    l.remove(l[0])
                    continue
                if l[0].startswith('f'):
                    file.append(l[0])
                    l.remove(l[0])
                    break
            if l[0] == "*":
                flag = False
                file = sorted(file)
                for j in file:
                    print(j)
                file = []
                count += 1
                l.remove(l[0])
                break
            elif l[0] == ']':
                count1 += 1
                l.remove(l[0])
                continue
            elif l[0].startswith('d') or l[0].startswith('f'):
                print("|     |     {}".format(l[0]))
                l.remove(l[0])
                continue
    if len(l) == 1 and l[0] == '#':
        flag1 = False
