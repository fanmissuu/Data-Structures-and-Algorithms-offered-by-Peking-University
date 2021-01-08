import copy

move = [[1,1,0,1,1,0,0,0,0],[1,1,1,0,0,0,0,0,0],[0,1,1,0,1,1,0,0,0],[1,0,0,1,0,0,1,0,0],[0,1,0,1,1,1,0,1,0],[0,0,1,0,0,1,0,0,1],[0,0,0,1,1,0,1,1,0],[0,0,0,0,0,0,1,1,1],[0,0,0,0,1,1,0,1,1]]
clock = []
for i in range(3):
    a = input().strip().split()
    for j in a:
        clock.append(int(j))
possible = []
for i1 in range(4):
    clock[0] = (clock[0] + i1) % 4
    clock[1] = (clock[1] + i1) % 4
    clock[3] = (clock[3] + i1) % 4
    clock[4] = (clock[4] + i1) % 4
    for i2 in range(4):
        clock[0] = (clock[0] + i2) % 4
        clock[1] = (clock[1] + i2) % 4
        clock[2] = (clock[2] + i2) % 4
        for i3 in range(4):
            clock[1] = (clock[1] + i3) % 4
            clock[2] = (clock[2] + i3) % 4
            clock[4] = (clock[4] + i3) % 4
            clock[5] = (clock[5] + i3) % 4
            b = copy.deepcopy(clock)
            if clock[0] == 0:
                i4 = 0
            else:
                i4 = 4 - clock[0]
            if clock[1] == 0:
                i5 = 0
            else:
                i5 = 4 - clock[1]
            if clock[2] == 0:
                i6 = 0
            else:
                i6 = 4 - clock[2]
            clock[3] = (clock[3] + i4 + i5) % 4
            if clock[3] == 0:
                i7 = 0
            else:
                i7 = 4 - clock[3]
            clock[6] = (clock[6] + i4 + i7) % 4
            if clock[6] == 0:
                i8 = 0
            else:
                i8 = 4 - clock[6]
            clock[4] = (clock[4] + i5 + i7) % 4
            clock[5] = (clock[5] + i5 + i6) % 4
            clock[7] = (clock[7] + i5 + i7 + i8) % 4
            clock[8] = (clock[8] + i6 + i8) % 4
            if clock[4] == clock[5] == clock[7] == clock[8]:
                if clock[4] == 0:
                    i9 = 0
                else:
                    i9 = 4 - clock[4]
                time = i1 + i2 + i3 + i4 +i5 + i6 + i7 + i8 + i9
                situation = [time, i1, i2, i3, i4, i5, i6, i7, i8, i9]
                possible.append(situation)
            clock = copy.deepcopy(b)
            clock[1] = (clock[1] - i3) % 4
            clock[2] = (clock[2] - i3) % 4
            clock[4] = (clock[4] - i3) % 4
            clock[5] = (clock[5] - i3) % 4
        clock[0] = (clock[0] - i2) % 4
        clock[1] = (clock[1] - i2) % 4
        clock[2] = (clock[2] - i2) % 4
    clock[0] = (clock[0] - i1) % 4
    clock[1] = (clock[1] - i1) % 4
    clock[3] = (clock[3] - i1) % 4
    clock[4] = (clock[4] - i1) % 4
possible = sorted(possible, key=lambda x:x[0])
s = ''
for i in range(1,10):
    if possible[0][i] != 0:
        for j in range(possible[0][i]):
            s += str(i)
print(' '.join(s))
