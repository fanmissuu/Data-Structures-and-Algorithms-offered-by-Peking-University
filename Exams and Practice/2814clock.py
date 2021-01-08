move = [[1,1,0,1,1,0,0,0,0],[1,1,1,0,0,0,0,0,0],[0,1,1,0,1,1,0,0,0],[1,0,0,1,0,0,1,0,0],[0,1,0,1,1,1,0,1,0],[0,0,1,0,0,1,0,0,1],[0,0,0,1,1,0,1,1,0],[0,0,0,0,0,0,1,1,1],[0,0,0,0,1,1,0,1,1]]
clock = []
for i in range(3):
    a = input().strip().split()
    for j in a:
        clock.append(int(j))

times = []
for i1 in range(4):
    clock[0] = (clock[0] + 1 * i1) % 4
    clock[1] = (clock[1] + 1 * i1) % 4
    clock[3] = (clock[3] + 1 * i1) % 4
    clock[4] = (clock[4] + 1 * i1) % 4
    for i2 in range(4):
        clock[0] = (clock[0] + 1 * i2) % 4
        clock[1] = (clock[1] + 1 * i2) % 4
        clock[2] = (clock[2] + 1 * i2) % 4
        for i3 in range(4):
            clock[1] = (clock[1] + 1 * i3) % 4
            clock[2] = (clock[2] + 1 * i3) % 4
            clock[4] = (clock[4] + 1 * i3) % 4
            clock[5] = (clock[5] + 1 * i3) % 4
            for i4 in range(4):
                clock[0] = (clock[0] + 1 * i4) % 4
                clock[3] = (clock[3] + 1 * i4) % 4
                clock[6] = (clock[6] + 1 * i4) % 4
                for i5 in range(4):
                    clock[1] = (clock[1] + 1 * i5) % 4
                    clock[3] = (clock[3] + 1 * i5) % 4
                    clock[4] = (clock[4] + 1 * i5) % 4
                    clock[5] = (clock[5] + 1 * i5) % 4
                    clock[7] = (clock[7] + 1 * i5) % 4
                    for i6 in range(4):
                        clock[2] = (clock[2] + 1 * i6) % 4
                        clock[5] = (clock[5] + 1 * i6) % 4
                        clock[8] = (clock[8] + 1 * i6) % 4
                        for i7 in range(4):
                            clock[3] = (clock[3] + 1 * i7) % 4
                            clock[4] = (clock[4] + 1 * i7) % 4
                            clock[6] = (clock[6] + 1 * i7) % 4
                            clock[7] = (clock[7] + 1 * i7) % 4
                            for i8 in range(4):
                                clock[6] = (clock[6] + 1 * i8) % 4
                                clock[7] = (clock[7] + 1 * i8) % 4
                                clock[8] = (clock[8] + 1 * i8) % 4
                                for i9 in range(4):
                                    clock[4] = (clock[4] + 1 * i9) % 4
                                    clock[5] = (clock[5] + 1 * i9) % 4
                                    clock[7] = (clock[7] + 1 * i9) % 4
                                    clock[8] = (clock[8] + 1 * i9) % 4
                                    #4**9种情况
                                    exist = False
                                    for i in clock:
                                        if i != 0:
                                            exist = True
                                            break
                                    if not exist:
                                        situation = []
                                        time = i1 + i2 + i3 + i4 +i5 + i6 + i7 + i8 + i9
                                        situation.append(time)
                                        situation.append(i1)
                                        situation.append(i2)
                                        situation.append(i3)
                                        situation.append(i4)
                                        situation.append(i5)
                                        situation.append(i6)
                                        situation.append(i7)
                                        situation.append(i8)
                                        situation.append(i9)
                                        times.append(situation)
                                    clock[4] = (clock[4] - 1 * i9) % 4
                                    clock[5] = (clock[5] - 1 * i9) % 4
                                    clock[7] = (clock[7] - 1 * i9) % 4
                                    clock[8] = (clock[8] - 1 * i9) % 4
                                clock[6] = (clock[6] - 1 * i8) % 4
                                clock[7] = (clock[7] - 1 * i8) % 4
                                clock[8] = (clock[8] - 1 * i8) % 4
                            clock[3] = (clock[3] - 1 * i7) % 4
                            clock[4] = (clock[4] - 1 * i7) % 4
                            clock[6] = (clock[6] - 1 * i7) % 4
                            clock[7] = (clock[7] - 1 * i7) % 4
                        clock[2] = (clock[2] - 1 * i6) % 4
                        clock[5] = (clock[5] - 1 * i6) % 4
                        clock[8] = (clock[8] - 1 * i6) % 4
                    clock[1] = (clock[1] - 1 * i5) % 4
                    clock[3] = (clock[3] - 1 * i5) % 4
                    clock[4] = (clock[4] - 1 * i5) % 4
                    clock[5] = (clock[5] - 1 * i5) % 4
                    clock[7] = (clock[7] - 1 * i5) % 4
                clock[0] = (clock[0] - 1 * i4) % 4
                clock[3] = (clock[3] - 1 * i4) % 4
                clock[6] = (clock[6] - 1 * i4) % 4
            clock[1] = (clock[1] - 1 * i3) % 4
            clock[2] = (clock[2] - 1 * i3) % 4
            clock[4] = (clock[4] - 1 * i3) % 4
            clock[5] = (clock[5] - 1 * i3) % 4
        clock[0] = (clock[0] - 1 * i2) % 4
        clock[1] = (clock[1] - 1 * i2) % 4
        clock[2] = (clock[2] - 1 * i2) % 4
    clock[0] = (clock[0] - 1 * i1) % 4
    clock[1] = (clock[1] - 1 * i1) % 4
    clock[3] = (clock[3] - 1 * i1) % 4
    clock[4] = (clock[4] - 1 * i1) % 4
times = sorted(times, key=lambda x:x[0])
s = ''
for i in range(1,10):
    if times[0][i] != 0:
        for j in range(times[0][i]):
            s += str(i)
print(' '.join(s))
