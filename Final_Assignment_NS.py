afstandKM = float(input('Afstand van uw treinrit in kilometers: '))
leeftijd = int(input('Uw leeftijd: '))
weekendrit = bool(input('Is het een weekendrit? (Ja=True/Nee=False): '))

def standaardprijs(afstandKM):
    if afstandKM < 50:
        prijs = 0.80 * afstandKM
    if afstandKM <= 0:
        prijs = 0
    else:
        prijs = 15 + (0.60 * afstandKM)
    return float(prijs)

def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == False and 65 <= leeftijd < 12:
        prijs = float((standaardprijs(afstandKM) * 0.70))
    if weekendrit == True and 65 <= leeftijd < 12:
        prijs = float((standaardprijs(afstandKM) * 0.65))
    if weekendrit == True and 65 > leeftijd >= 12:
        prijs = float((standaardprijs(afstandKM) * 0.60))
    if weekendrit == False and 65 > leeftijd >= 12:
        prijs = float(standaardprijs(afstandKM))
    return float(prijs)
print('De definitieve prijs is: €' + str(float(ritprijs(leeftijd, weekendrit, afstandKM))))