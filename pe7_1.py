gradenC = float(input('Temperatuur in Celsius:'))
def convert(tem5_1):
    gradenF = gradenC * 1.8 + 32
    return gradenF

print('Temperatuur in Fahrenheit:' + str(convert(gradenC)))

def table(tem5_1):
    print('{:7} {:7}'.format('F', 'C'))
    for i in range(-30, 50, 10):
        print('{:7} {:7.1f}'.format(i * 1.8 + 32, i))

table(gradenC)