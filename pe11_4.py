import csv
def artikels_toevoegen():
     with open('producten.csv', 'w', newline='') as artikel:
        fieldnames = ['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs']
        writer = csv.DictWriter(artikel, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Artikelnummer': 121, 'Artikelcode': 'ABC123', 'Naam': 'Highlight pen', 'Voorraad': 231, 'Prijs': 0.56})
        writer.writerow({'Artikelnummer': 123, 'Artikelcode': 'PQR678', 'Naam': 'Nietmachine', 'Voorraad': 587, 'Prijs': 9.99})
        writer.writerow({'Artikelnummer': 128, 'Artikelcode': 'ZYX163', 'Naam': 'Bureaulamp', 'Voorraad': 34, 'Prijs': 19.95})
        writer.writerow({'Artikelnummer': 137, 'Artikelcode': 'MLK709', 'Naam': 'Monitorstandaard', 'Voorraad': 66, 'Prijs': 32.50})
        writer.writerow({'Artikelnummer': 271, 'Artikelcode': 'TR665', 'Naam': 'Ipad hoes', 'Voorraad': 155, 'Prijs': 19.01})

artikels_toevoegen()

with open('producten.csv', 'r') as product:
    reader = csv.DictReader(product, delimiter=';')
    productLijst = []
    prijsLijst = []
    voorraadLijst = []
    for row in reader:
        prijsLijst += [float(row['Prijs'])]
        productLijst += [row]
        voorraadLijst += [int(row['Voorraad'])]

    min_voorraad = min(voorraadLijst)
    hoogste_prijs = max(prijsLijst)
    totale_voorraad = sum(voorraadLijst)

    for art in productLijst:
        if min_voorraad == int(art['Voorraad']):
            print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(art['Voorraad'], art[
                'Artikelnummer']))
        if hoogste_prijs == float(art['Prijs']):
            print('Het duurste artikel is {} en die kost {} Euro'.format(art['Naam'], art['Prijs']))

print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totale_voorraad))