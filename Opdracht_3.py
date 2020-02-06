def count(number, countlist):
    i = 0
    for item in countlist:
        if item == number:
            i += 1
        else:
            continue

    return i


# Tussen welke 2 getallen is het verschil
def diffBigIndex(lst):
    highest = 0
    i = 0
    while i < len(lst) - 1:
        diff = lst[i] - lst[i + 1]

        if highest < abs(diff):
            highest = diff
        i += 1

    return highest


def lstCheck(lst):
    zeroCount = count(0, lst)
    oneCount = count(1, lst)
    print(zeroCount, oneCount)
    if oneCount > zeroCount:
        if zeroCount < 12:
            return True
        else:
            return False
    else:
        return False