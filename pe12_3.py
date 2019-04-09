import xmltodict
with open('stationslijsten.xml') as file:
    document = xmltodict.parse(file.read())

    print('Dit zijn de codes en types van de 4 stations:')
    for station in document['Stations']['Station']:
        print('{0:4} - {1}'.format(station['Code'], station['Type']))

    print('\nDit zijn alle stations met één of meer synoniemen:')
    for station in document['Stations']['Station']:
        if(station['Synoniemen']):
            synoniemen = station['Synoniemen']['Synoniem']
            print('{0:4} - {1}'.format(station['Code'], ', '.join(synoniemen)))

    print('\nDit is de lange naam van elk station:')
    for station in document['Stations']['Station']:
        print('{0:4} - {1}'.format(station['Code'], station['Namen']['Lang']))