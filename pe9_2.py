while True:
    letters = input('Geef een string van vier letters: ')
    if len(letters) == 4:
        print('Inlezen van correcte string: ' + str(letters) + ' is geslaagd')
        break
    else:
        lengteL = len(letters)
        print(str(letters) + ' heeft ' + str(lengteL) + ' letters')