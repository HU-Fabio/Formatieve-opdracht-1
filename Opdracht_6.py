def avg(lst):
    lenght = len(lst)
    count = 0
    for i in range(0, lenght):
        count += lst[i]

    return count / lenght


def avgDimensional(lst):
    lenght = len(lst)
    count = 0
    division = 0
    for i in range(0, lenght):
        if type(lst[i]) == list:
            lenght2 = len(lst[i])
            division += lenght + lenght2 - 1
            for i2 in range(0, lenght2):
                count += lst[i][i2]
        else:
            count += lst[i]

    return count / division