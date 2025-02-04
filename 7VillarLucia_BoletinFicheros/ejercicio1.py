#Escribe un programa que escriba los 100 primeros números naturales en el archivo numeros.txt.
with open("numeros.txt",encoding="utf-8",mode="w") as f:
    for i in range(0,101):
        if(i<100):
            f.write(str(i)+",")
        else:
            f.write(str(i))