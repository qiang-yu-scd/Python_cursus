zin5_5 = input('Voer een willekeurige zin in: ')
def gemiddelde(invoer):
    lst5_5 = [len(x) for x in invoer.split()]
    gem5_5 = sum(lst5_5) / len(lst5_5)
    return round(gem5_5, 2)
print('De gemiddelde lengte van de woorden in de zin: ' + str(gemiddelde(zin5_5)))