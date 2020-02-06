def palinDroom(text):
    reverse = text[::-1]
    if reverse.capitalize() == text.capitalize():
        return True
    else:
        return False


def palinDroomLib(text):
    reverse = ''.join(reversed(text))
    if reverse.capitalize() == text.capitalize():
        return True
    else:
        return False


print(palinDroomLib('kok'))