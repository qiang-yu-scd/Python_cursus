import xmltodict
with open('producten.xml') as fd:
    document = xmltodict.parse(fd.read())
    for artikel in document['artikelen']['artikel']:
        print(artikel['naam'])

