def rotateMatrix(a):
    for layer in range(len(a) // 2):
        first = layer
        last = len(a) - 1 - layer
        for i in range(first, last):
            offset = i - first

            top = a[first][i]  # temp = top
            a[first][i] = a[last - offset][first]  # top = left
            a[last - offset][first] = a[last][last - offset]  # left = bottom
            a[last][last - offset] = a[i][last]  # bottom = right
            a[i][last] = top  # right = temp
    return a


print(rotateMatrix([[1, 2, 3, 4], [5, 6, 7, 8],
                    [9, 10, 11, 12], [13, 14, 15, 16]]))
