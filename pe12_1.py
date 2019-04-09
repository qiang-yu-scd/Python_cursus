import xmltodict
with open('producten.xml') as bestand:
    document = xmltodict.parse(bestand.read())
    for artikel in document['artikelen']['artikel']:
        print(artikel['naam'])