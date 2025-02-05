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
        contenidoMenor=""
        contenidoMayor=""
        with open(fichero,encoding="utf-8") as f:
            linea=f.readline()
            while(linea):
                count=0
                for caracter in linea.replace("\n","").replace(" ",""):
                    count+=1
                if(count<corte):
                   contenidoMenor+=linea
                else:
                    contenidoMayor+=linea
                linea=f.readline()
            with open("menor.txt",mode="w") as fm:
                        fm.write(contenidoMenor)
            with open("mayor.txt",mode="w") as fy:
                        fy.write(contenidoMayor)

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

    
