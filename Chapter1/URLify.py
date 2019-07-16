def URLify(a, b):
    c = ""
    for i in range(b):
        if (a[i] == ' ' or a[i] == '\n'):
            c += "%20"
        else:
            c += a[i]
    return c


print(URLify("Mr John Smith", 13))
