def zeroMatrix(a):
    rowflags = [0 for i in range(len(a))]
    columnflags = [0 for i in range(len(a[0]))]

    for row in range(len(a)):
        for col in range(len(a[0])):
            if a[row][col] == 0:
                rowflags[row] = 1
                columnflags[col] = 1

    for i in range(len(rowflags)):
        if rowflags[i] == 1:
            for col in range(len(a[i])):
                a[i][col] = 0

    for j in range(len(columnflags)):
        if columnflags[j] == 1:
            for row in range(len(a)):
                a[row][i] = 0

    return a


print(zeroMatrix([[1, 0], [1, 1]]))
