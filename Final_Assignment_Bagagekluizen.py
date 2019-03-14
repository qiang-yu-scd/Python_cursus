print('Menu\n1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug')


def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    lstRegels = infile.readlines()
    aantalkluizen = len(lstRegels)
    return aantalkluizen
aantalkluizen = toon_aantal_kluizen_vrij()
print('Aantal vrije kluizen zijn:' + str(aantalkluizen))

def nieuwe_kluis():
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    infile = open('kluizen.txt')
    regels = infile.readlines()
    for regel in regels:
        onderdelen = regel.split(',')
        kluisnr = int(onderdelen[0])
        kluisnummers.remove(kluisnr)

#def kluis_openen():

#def kluis_teruggeven():

keuze = int(input('Welke keuze?'))
if keuze == 1:
    vrijekluizen = toon_aantal_kluizen_vrij()
    print(vrijekluizen)
elif keuze == 2:
    nieuwekluis = nieuwe_kluis()
elif keuze == 3:
    kluis_openen()
elif keuze == 4:
    kluis_teruggeven()