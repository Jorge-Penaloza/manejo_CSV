import os
ejemplo_dir = '/Users/ricar/Google Drive/IACC/2021/Programacion avanzada 2/Semana 8/'
contenido = os.listdir(ejemplo_dir)
pdf = []
for fichero in contenido:
    fichero.endswith(".pdf")
    print(fichero, "es" if fichero.endswith(".pdf") else "no es", "PDF")
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.pdf'):
        pdf.append(fichero)
print()
for fichero in pdf:
    print(fichero, "es un archivo con extension PDF")