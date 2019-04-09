x = input('Naam: ')
y = input('Beginstation: ')
z= input('Eindstation: ')
invoerstring = x + y + z

def code(invoerstring):
    for i in invoerstring:
        print(chr(ord(i)+3), sep ='', end = '')

code(invoerstring)