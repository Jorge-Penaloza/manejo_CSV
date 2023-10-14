import csv
class archivoCSV:
    def __init__(self, archivo):
        self.archivo = archivo
    
    def setFile(self, archivo):
        self.archivo = archivo
    
    def getFile(self):
        return self.archivo
    
    def crearCabecera(self, *arg):
        archivo = open(self.archivo,"w", newline="")
        escribir = csv.writer(archivo, delimiter=',', quoting=csv.QUOTE_MINIMAL) 
        escribir.writerow(arg)
        
    def insertar(self, *arg):
        archivo = open(self.archivo,"a", newline="")
        escribir = csv.writer(archivo, delimiter=',',  quoting=csv.QUOTE_MINIMAL)  
        escribir.writerow(arg)
        
    def listar(self ):
        with open(self.archivo, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

        