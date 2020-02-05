# Schrijf een programma dat een piramide van variabele lengte afdrukt, zoals in het voorbeeld.
# Druk ieder character apart af.
# De gebruiker geeft aan hoe groot de piramide is.
# Implementeer je programma twee keer, de eerste keer met twee for loops, en daarna met twee while loops. Maak ook versies die de pyramide een andere kant op laten wijzen.


def pyramidFor(length):
    for i in range(1, length + 1):
        print('*' * i)

    for i in range(length - 1, 0, -1):
        print('*' * i)


def pyramidWhile(length):
    i = 1
    while i < length:
        print('*' * i)
        i = i + 1

    while length:
        print('*' * length)
        length = length - 1


def pyramidForREV(length):
    for i in range(1, length + 1):
        item = '*' * i
        print(f"{item:>{(length + 1) - 1}s}")

    for i in range(length - 1, 0, -1):
        item = '*' * i
        print(f"{item:>{(length + 1) - 1}s}")


def pyramidWhileREV(length):
    i = 1
    while i < length:
        item = '*' * i
        print(f"{item:>{(length + 1) - 1}s}")
        i = i + 1

    while length:
        item = '*' * length
        print(f"{item:>{4}s}")
        length = length - 1


pyramidHeight = int(input('Hoe hoog moet de pyramide zijn?'))

pyramidWhileREV(pyramidHeight)
