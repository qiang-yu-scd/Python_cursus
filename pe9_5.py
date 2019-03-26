import sys
studenten = {}
while True:
    newStudent = input('Volgende naam: ')
    def namen(nS):
        i = 0
        if nS == '':
            for item in studenten.items():
                names = list(studenten.keys())
                name = names[i]
                count = studenten[name]
                i += 1
                if int(count) == 1:
                    print('Er is ' + str(studenten[name]) + ' student met de naam ' + str(name))
                elif int(count) > 1:
                    print('Er zijn ' + str(studenten[name]) + ' studenten met de naam ' + str(name))
        elif nS in studenten.keys():
            add = int(studenten[nS]) + 1
            studenten[nS] = add
        elif nS not in studenten.keys():
            studenten[nS] = 1

    namen(newStudent)

