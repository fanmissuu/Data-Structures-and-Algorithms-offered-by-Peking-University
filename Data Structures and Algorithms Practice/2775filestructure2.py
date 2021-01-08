#import pdb

#inputs = ['ROOT', 'file1', 'file2', 'dir3', 'dir2', 'file1', 'file2', ']', ']', 'file4', 'dir1', ']', 'file3', ']']

def my_print(s, n):
    out = ''
    for i in range(n):
        out += '|     '
    out += s
    print(out)

def func(inputs, l, r, n):
    my_print(inputs[l], n)

    files = []
    bg = -1
    diff = 0

    for k in range(l + 1, r):
        if inputs[k][0] == 'd':
            diff += 1
        elif inputs[k][0] == ']':
            diff -= 1

        if diff == 1 and inputs[k][0] == 'd':
            bg = k
        if diff == 0:
            if bg == -1:
                files.append(inputs[k])
            else:
                func(inputs, bg, k, n + 1)
                bg = -1

    files = sorted(files)
    for f in files:
        my_print(f, n)

cases = 0
lines = ['ROOT']
while True:
    line = input().strip()

    if line == '*':
        cases += 1
        print('DATA SET {}:'.format(cases))
        func(lines, 0, len(lines), 0)
        print()
        lines = ['ROOT']

    elif line == '#':
        break

    else:
        lines += [line]
