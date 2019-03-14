bruin = {"Boxtel", "Best", "Beukenlaan", "Eindhoven", "Helmond 't Hout", "Helmond", "Helmond Brouwhuis", "Deurne"}
groen = {"Boxtel", "Best", "Beukenlaan", "Eindhoven", "Geldrop", "Heeze", "Weert"}
overeenkomst = bruin & groen
verschil = bruin - groen
samenvoegen = bruin | groen
print('Stations die overeenkomst: ' + str(overeenkomst))
print('Stations die verschillen van elkaar: ' + str(verschil))
print('Alle stations: ' + str(samenvoegen))