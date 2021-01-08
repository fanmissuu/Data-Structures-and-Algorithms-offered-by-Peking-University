import copy
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
        eve_line.append(0)
    for i in range(len1+1):
        maxLen.append(copy.deepcopy(eve_line))

    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if str1[i-1] == str2[j-1]:
                maxLen[i][j] = maxLen[i-1][j-1] + 1
            else:
                maxLen[i][j] = max(maxLen[i-1][j], maxLen[i][j-1])
    print(maxLen[len1][len2])
