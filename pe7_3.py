teller5_3 = 0
with open('kaartnummers.txt') as k:
    for gegevens in k:
        teller5_3 += 1
    print('Deze file telt ' + str(teller5_3) + ' regels')

