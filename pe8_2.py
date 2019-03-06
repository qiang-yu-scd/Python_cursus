inlezenStr = eval(input("Geef lijst met minimaal 10 strings: "))
nieuwLijst = []
i = 0
for woord in inlezenStr:
    if (len(inlezenStr[i]) == 4):
        nieuwLijst.append(inlezenStr[i])
    i += 1

print('De nieuw-gemaakte lijst met alle vier-letter strings is:' + str(nieuwLijst))


