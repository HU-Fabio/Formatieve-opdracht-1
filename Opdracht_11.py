def caesar():
    # Source: https://stackoverflow.com/questions/14424500/text-shift-function-in-python
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    unencrypted = input('Geef een tekst:')
    rotation = int(input('Geef een rotatie:'))
    translation = []

    for ch in unencrypted:
        # Checken of het geen spatie is en of de letter in het alphabet zit
        if ch != ' ' and ch in alphabet:
            translation.append(alphabet[(alphabet.index(ch) + rotation) % 26])
        else:
            translation.append(ch)
    # Voeg de lijst van translatie bij elkaar en maak er een nette string van
    return ''.join(translation)