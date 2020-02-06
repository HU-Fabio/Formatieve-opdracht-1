def sortList(lst):
    len = lst.__len__() - 1
    count = 0
    while count < len:
        for i in range(0, len):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                continue
        count += 1

    return lst