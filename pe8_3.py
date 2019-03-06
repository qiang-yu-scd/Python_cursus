invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoerLst = invoer.split('-')
invoerG = list(map(int, invoerLst))
invoerG.sort()
maxLijst = max(invoerG)
minLijst = min(invoerG)
aantalG = len(invoerG)
somG = sum(invoerG)
gemG = somG / aantalG

print('Gesorteerde list van ints: ' + str(invoerG) + '\n' + 'Grootste getal: ' + str(maxLijst) + ' en Kleinste getal: ' + str(minLijst) + '\n' + 'Aantal getallen: ' + str(aantalG) + ' en Som van de getallen: ' + str(somG) + '\n' + 'Gemiddelde: ' + str(gemG))