infile = open('kluizen.txt', 'w')
infile.close()

menu = eval(input('1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug'))

if menu == 1:
    def toon_aantal_kluizen_vrij(optie):
        kluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        vrijKluizen = {}
        for kluis in kluizen:
            if kluis in vrijKluizen:
                vrijKluizen += 1
            else:
                vrijKluizen + 0
        print(vrijKluizen)

