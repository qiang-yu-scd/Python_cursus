try:
    Aantal = int(input('Het aantal personen dat mee op reis gaat: '))
    bedragPerP = 4356 / Aantal
    if Aantal < 0:
        print('Aantal - Negatieve getallen zijn niet toegestaan!')
    else:
        print(bedragPerP)
except ZeroDivisionError:
    print('Aantal = 0 - Delen door nul kan niet!')
except ValueError:
    print('Aantal - Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Alle andere fouten: - Onjuiste invoer!')

