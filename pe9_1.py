getalLijst = []
while True:
    getal = float(input('Geef een getal: '))
    if getal != 0:
        getalLijst.append(getal)
        aantal9_1 = len(getalLijst)
        som9_1 = sum(getalLijst)
    else:
        break
print('Er zijn ' + str(aantal9_1) + ' getallen ingevoerd, de som is: ' + str(som9_1))