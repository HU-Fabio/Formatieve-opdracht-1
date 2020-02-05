def TextComparing():
    text = input('Geef een string:')
    text2 = input('Geef een string:')

    length = min(len(ele) for ele in [text,text2])

    for i in range(0, length):
        if i == (length - 1):
            print('De strings zijn het zelfde')
        elif text[i] != text2[i]:
            print('Het eerste verschil zit op index: ' + str(i))
            break


TextComparing()
