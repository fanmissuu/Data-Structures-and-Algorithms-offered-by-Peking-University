
import copy

def check(clock):
    flag = True
    for j in clock:
        if j % 4 != 0:
            flag = False
            break
    return flag

best_result = [1000000, []]

def search(method_id,clock):
    if method_id == 9:
        if check(clock):
            num_moves = sum(move_clock)
            if num_moves < best_result[0]:
                best_result[0] = num_moves
                best_result[1] = copy.deepcopy(move_clock)
        return

    for i in range(4):
        for d in range(9):
            clock[d] = clock[d] + method[method_id][d] * i
        move_clock[method_id] = i
        if sum(move_clock) > best_result[0]:
            return
        search(method_id + 1, clock)
        for c in range(9):
            clock[c] = clock[c] - method[method_id][c] * i
        move_clock[method_id] -= i
    return


move_clock = [0,0,0,0,0,0,0,0,0]
method = [[1,1,0,1,1,0,0,0,0],[1,1,1,0,0,0,0,0,0],[0,1,1,0,1,1,0,0,0],[1,0,0,1,0,0,1,0,0],[0,1,0,1,1,1,0,1,0],[0,0,1,0,0,1,0,0,1],[0,0,0,1,1,0,1,1,0],[0,0,0,0,0,0,1,1,1],[0,0,0,0,1,1,0,1,1]]
clock = []
for i in range(3):
    a = input().strip().split()
    for j in a:
        clock.append(int(j))

search(0,clock)

s = ''
for v in range(9):
    if best_result[1][v] != 0:
        for j in range(best_result[1][v]):
            s += str(v+1)
print(' '.join(s))
