oldpassword = input('Voer hier je oude wachtwoord in: ')
newpassword = input('Voer hier je nieuwe wachtwoord in: ')
def password(newpassword, oldpassword):
    if len(newpassword) < 6 or newpassword == oldpassword:
        print('New password invalid')
        return False
    else:
        print('New password succeeded')
        return True

print(password(newpassword, oldpassword))