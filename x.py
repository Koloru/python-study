size = 10

for i in range(size):
    print('[', end='')
    for j in range(size):
        if i == j:
            print('X', end=' ')
        elif i + j == size - 1:
            print(i + j, end=' ')
        else:
            print(' ', end=' ')
    print(']', end='')
    print()
