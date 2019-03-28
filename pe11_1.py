try:
    Aantal = abs(input('Het aantal personen dat mee op reis gaat: '))
    bedragPerP = 4356 / Aantal
except ZeroDivisionError:
    print('Aantal = 0 - Delen door nul kan niet!')
except TypeError:
    print('Aantal - Negatieve getallen zijn niet toegestaan!')
except ValueError:
    print('Aantal - Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Alle andere fouten: - Onjuiste invoer!')