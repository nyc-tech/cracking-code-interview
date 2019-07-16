from collections import defaultdict


def checkPermutation(a, b):
    if (sorted(a) == sorted(b)):
        return True
    return False


def checkPermutationHash(a, b):
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
    for i in a:
        dict1[i] += 1
    for v in b:
        dict2[v] += 1
    return True if dict1 == dict2 else False


print(checkPermutation("test", "tset"))

print(checkPermutation("test", "tst"))

print(checkPermutationHash("test", "tset"))

print(checkPermutationHash("test", "tst"))
