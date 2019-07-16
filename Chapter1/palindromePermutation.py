from collections import defaultdict


def palindromePermutation(a):
    dict1 = defaultdict(int)
    # need to produce all variations of permutations and build table from bottom up
    for i in a.lower():
        dict1[i] += 1
    print(dict1)
    for k, v in dict1.items():
        if v % 2 == 1 and v != 1:
            return False
    return True


print(palindromePermutation("Tact Coa"))
