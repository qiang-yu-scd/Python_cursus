infile = open('tickersymbol.txt', 'a')
bedrijf = input('Naam bedrijf: ')
symbool = input('Het ticker symbool: ')
infile.write(str(bedrijf) + ': ' + str(symbool) + '\n')
infile.close()

#def ticker(filename):
