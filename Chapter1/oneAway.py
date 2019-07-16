def oneAway(a, b):
    if len(a) == len(b):
        # MAKE SURE YOU RETURN THE FUNCTIONS, otherwise it will always return FALSE
        return checkReplace(a, b)
    # check to see if left hand side is larger or smaller than right hand side
    elif (len(a) + 1) == len(b):
        return checkInsert(a, b)
    elif (len(a) - 1) == len(b):
        # if LHS is larger by one, then switch arguments to formula since formula checks to see if LHS can be inserted to be equal to RHS
        return checkInsert(b, a)
    else:
        return False


def checkReplace(str1, str2):
    counter = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if counter == 1:
                return False
            counter += 1
    return True


def checkInsert(str1, str2):
    # insert into str1 to make str2
    index1 = 0
    index2 = 0
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if (index1 != index2):
                return False
            index2 += 1
        else:  # str1[index1] and str2[index2] are the same
            index1 += 1
            index2 += 1
    return True


print(oneAway('pale', 'ple') == True)
print(oneAway('pales', 'pale') == True)
print(oneAway('pale', 'bale') == True)
print(oneAway('pale', 'bake') == False)
