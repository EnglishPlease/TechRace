n = int(input())

for i in range(1, n + 1):

    if i % 15 == 0:
        print(", Tech Race", end='')

    elif i % 3 == 0:
        print(", Tech", end='')

    elif i % 5 == 0:
        print(", Race", end='')

    elif i != 1:
        print(", ", i, end='', sep='')
    else:
        print(i, end='')

