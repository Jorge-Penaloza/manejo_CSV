with open("miarchivo.txt","rb") as f:
    data = f.read()
    
for elemento in data:
    print(elemento, chr(elemento))