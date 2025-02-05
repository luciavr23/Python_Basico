#Escriba un programa que se encargue de clasificar una serie de cadenas atendiendo a su longitud. 
# Se solicitará al usuario el nombre del archivo que contendrá el conjunto de palabras, cada una en una línea. 
# También se pedirá por teclado un valor entero que se utilizará como valor de corte para clasificar las palabras 
# del archivo anterior. Las palabras con longitud menor al valor de corte se almacenarán en el fichero menor.txt y 
# el resto de palabras en el fichero mayor.txt
import os
def clasificaPalabras(nombreFich):
    if(os.path.isfile(nombreFich)):
        corte=int(input("Introduzca la longitud de corte: "))
        count=0
        with open(fichero,encoding="utf-8") as f:
            linea=f.readline()
            while(linea):
                count=0
                for f in linea:
                    count+=1
                if(count<corte):
                    with open("menor.txt",mode="a") as fm:
                        fm.write(linea)
                else:
                    with open("mayor.txt",mode="a") as fy:
                        fy.write(linea)
                linea=f.readline()

    else:
        print("El fichero no existe")



fichero=input("Introduzca el nombre del fichero a leer: ")
punto=fichero.rfind(".")
if(punto!=-1):
    formato=fichero[punto:]
else:
    fichero=fichero+".txt"
    formato=".txt"

if(formato == ".txt"):
    clasificaPalabras(fichero)

    

