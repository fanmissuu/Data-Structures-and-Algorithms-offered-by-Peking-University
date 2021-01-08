#import pdb

#inputs = ['ROOT', 'file1', 'file2', 'dir3', 'dir2', 'file1', 'file2', ']', ']', 'file4', 'dir1', ']', 'file3', ']']

def my_print(s, n):
    out = ''
    for i in range(n):
        out += '|     '
    out += s
    print(out)

def func(inputs, pst, n):
    my_print(inputs[pst], n)

    files = []

    k = pst + 1
    while k < len(inputs):
        if inputs[k][0] == 'f':
            files.append(inputs[k])
        elif inputs[k][0] == 'd':
            new_pst = func(inputs, k, n + 1)
            k = new_pst
        elif inputs[k][0] == ']':
            files = sorted(files)
            for f in files:
                my_print(f, n)
            return k
        k += 1

cases = 0
lines = ['ROOT']
while True:
    line = input().strip()

    if line == '*':
        cases += 1
        print('DATA SET {}:'.format(cases))
        lines += [']']
        func(lines, 0, 0)
        print()
        lines = ['ROOT']

    elif line == '#':
        break

    else:
        lines += [line]
