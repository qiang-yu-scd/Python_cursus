oldpassword = input ('Voer hier je oude wachtwoord in: ')
newpassword = input ('Voer hier je nieuwe wachtwoord in: ')
def new_password(wachtwoord):
    if str(oldpassword) != str(wachtwoord) and len(wachtwoord) >= 6 :
        print('True')
    else:
        print('False')
    return new_password

new_password(newpassword)