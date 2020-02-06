import binascii


def shift(ch, n):
    # Source: https://stackoverflow.com/questions/18815820/convert-string-to-binary-in-python
    # de ord functie convert de character naar ASCII, format convert de ASCII naar Binary en de join brengt het weer samen in een string
    binaryCH = int(' '.join(format(ord(x), 'b') for x in ch))

    print(binaryCH << n)
    return binaryCH


print(shift('c', 2))