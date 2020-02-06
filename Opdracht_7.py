import random

def guess():
    number = random.randrange(10)
    numberGuess = None
    count = 0

    while numberGuess != number:
        numberGuess = int(input('Welk getal gok je?'))
        count += 1
    print('Het getal was:' + str(number))
    print('Je deed er: ' + str(count) + ' beurten over!')


guess()