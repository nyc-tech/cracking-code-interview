from collections import defaultdict


def isUnique(a):
    dict1 = defaultdict(int)
    for i in a:
        if (dict1[i]):
            return False
        dict1[i] += 1
    return True


print(isUnique('aab'))
print(isUnique('abcdef'))
