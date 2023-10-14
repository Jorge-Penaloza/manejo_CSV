import csv
 
file = open('miarchivo.csv', "r")  
reader = csv.reader(file, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
for row in reader:
    for columna in row:
        print(columna, end=" - ")
    print()