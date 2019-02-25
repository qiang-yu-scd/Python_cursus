afstandKM = float(input('Afstand van uw treinrit in kilometers: '))
leeftijd = int(input('Uw leeftijd: '))
wkdrit = input('Is het een weekendrit? (ja/nee invoeren): ')
if wkdrit == 'ja':
    weekendrit = True
if wkdrit == 'nee':
    weekendrit = False

def standaardprijs(afstandKM):
    if afstandKM < 50:
        tarief = 0.80 * afstandKM
    elif afstandKM <= 0:
        tarief = 0
    else:
        tarief = 15 + (0.60 * afstandKM)
    return tarief

def ritprijs(leeftijd, weekendrit, afstandKM):
    if not weekendrit and (leeftijd >= 65 or leeftijd < 12):
        tarief = standaardprijs(afstandKM) * 0.70
    elif weekendrit and (leeftijd >= 65 or leeftijd < 12):
        tarief = standaardprijs(afstandKM) * 0.65
    elif weekendrit and (leeftijd < 65 or leeftijd >= 12):
        tarief = standaardprijs(afstandKM) * 0.60
    elif not weekendrit and (leeftijd < 65 or leeftijd >= 12):
        tarief = standaardprijs(afstandKM)
    return tarief

print('De definitieve prijs is: €{:7.2f}'.format(round(ritprijs(leeftijd, weekendrit, afstandKM),2)))