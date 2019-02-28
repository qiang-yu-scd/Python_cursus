infile = open('hardlopers.txt', 'a')
from datetime import datetime
tijd = datetime.strftime(datetime.now(),'%A %d %B %Y %H:%M:%S')

name = input('Naam hardloper: ')
infile.write(tijd + ', ' + str(name) + '\n')
infile.close()
