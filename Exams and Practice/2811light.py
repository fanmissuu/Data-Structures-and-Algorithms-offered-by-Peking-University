
puzzle = [[0,0,0,0,0,0,0,0]]
count = 0
while count < 5:
    a = input().strip().split()
    b = [0,0,0,0,0,0,0,0]
    for i in range(6):
        b[i+1] = int(a[i])
    puzzle.append(b)
    count += 1
#puzzle变为0，1数字矩阵 大list套小list  6行8列

press = []
count = 0
while count < 6:
    press.append([0,0,0,0,0,0,0,0])
    count += 1

if_done = False
for i1 in range(2):
    if if_done:
        break
    for i2 in range(2):
        if if_done:
            break
        for i3 in range(2):
            if if_done:
                break
            for i4 in range(2):
                if if_done:
                    break
                for i5 in range(2):
                    if if_done:
                        break
                    for i6 in range(2):
                        if if_done:
                            break
                        press[1][1] = i1
                        press[1][2] = i2
                        press[1][3] = i3
                        press[1][4] = i4
                        press[1][5] = i5
                        press[1][6] = i6
                        #64种情况
                        for r in range(1,5):
                            for c in range(1,7):
                                press[r+1][c] = (puzzle[r][c] + press[r][c] + press[r][c-1] + press[r][c+1] + press[r-1][c]) % 2

                        exist = False
                        for c in range(1,7):
                            if (press[5][c-1] + press[5][c] + press[5][c+1] + press[4][c]) % 2 != puzzle[5][c]:
                                exist = True
                                break

                        if not exist:
                            if_done = True
                            for i in range(1,6):
                                b = str(press[i]).replace(',','')
                                print(b[3:-3])
