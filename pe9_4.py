import sys
myfile = open('tickersymbool.txt', 'r')
while True:
        def ticker(filename):
            tickerDict = {}
            for line in filename.readlines():
                cmp = line.split(":")[0].rstrip()
                code = line.split(":")[1].rstrip()
                tickerDict[cmp] = code.rstrip()
            return tickerDict

        info = ticker(myfile)
        def getInfo(bedrijf):
            s = ''
            for cmp, code in info.items():
                if bedrijf.upper().rstrip() == cmp.upper().rstrip():
                    s = ('Ticker symbol: ' + str(code) + '\n')
                    break
                elif bedrijf.upper().rstrip() == code.upper().rstrip():
                    s = ('Company name: ' + str(cmp))
                    break
                else:
                    s = ('Input not found! ' )
            return s

        bedrijf = input('Enter Company Name: ')
        print(getInfo(bedrijf))
        symbool = input('Enter Ticker Symbol: ')
        print(getInfo(symbool))
        sys.exit()