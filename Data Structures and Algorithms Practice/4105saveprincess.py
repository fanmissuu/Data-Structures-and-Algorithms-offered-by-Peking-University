import copy
T = int(input())
for t in range(T):
    line = input().strip().split()
    R = int(line[0])
    C = int(line[1])
    K = int(line[2])
    map = []
    for eve_line in range(R):
        map.append(copy.deepcopy(input().strip()))
    print(map)
