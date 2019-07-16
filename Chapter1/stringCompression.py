def stringCompression(a):
    compressedString = ""
    count = 0
    for i in range(len(a)):
        count += 1
        if (i+1) == len(a):
            compressedString += a[i]
            compressedString += str(count)
            return compressedString
        if a[i+1] != a[i]:
            compressedString += a[i]
            compressedString += str(count)
            count = 0


print(stringCompression('aabcccccaaa') == 'a2b1c5a3')
