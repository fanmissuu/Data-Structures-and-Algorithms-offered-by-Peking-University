import copy

def func(i,j):
    if maxLen[i][j] != -1:
        return maxLen[i][j]
    if i*j==0:
        maxLen[i][j] = 0
        return maxLen[i][j]
    if str1[i-1] == str2[j-1]:
        maxLen[i][j] = func(i-1,j-1) + 1
        return maxLen[i][j]
    else:
        maxLen[i][j] = max(func(i-1,j),func(i,j-1))
        return maxLen[i][j]


count = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    data_set = line.strip().split()
    str1 = data_set[0].strip()
    str2 = data_set[1].strip()
    len1 = len(str1)
    len2 = len(str2)
    maxLen = []
    eve_line = []
    for i in range(len2+1):
        eve_line.append(-1)
    for i in range(len1+1):
        maxLen.append(copy.deepcopy(eve_line))
    print(func(len1,len2))
