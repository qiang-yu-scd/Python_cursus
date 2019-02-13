leeftijd = input ('Geef je leeftijd: ')
print('1. ja')
print('2. nee')
paspoort = input ('Nederlands paspoort: ')
if int(leeftijd) >= 18 and paspoort == str(1) :
    print ('Gefeliciteerd, je mag stemmen!')
else :
    print ('Sorry, je mag niet stemmen!')