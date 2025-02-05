#Implementar un programa que permita realizar la operación de copia de un fichero. 
#Tanto origen.txt como destino.txt serán ficheros de texto cuyos nombres indicará el usuario por teclado.
import os
nombreOrigen=input("Indica el nombre del fichero que desea copiar: ")
nombreCopia=input("Indica el nombre que desea ponerle al fichero copiado: ")
lastIndexO= nombreOrigen.rfind(".")
lastIndexC= nombreCopia.rfind(".")
origen=False
copia=False

####CONTROLAR QUE EL NOMBRE DEL FICHERO ORIGEN SEA .TXT#####
if lastIndexO != -1:
    formato = nombreOrigen[lastIndexO:]
    if(formato != ".txt"):
       print("El fichero origen no es de texto,se obtuvo: "+formato+" y se esperaba .txt")
    else:
        origen=True
else:
    nombreOrigen+=".txt"
    origen=True

####CONTROLAR QUE EL NOMBRE DEL FICHERO COPIA SEA .TXT#####
if lastIndexC != -1:
    formato = nombreCopia[lastIndexC:]
    if(formato != ".txt"):
       print("El fichero copia no es de texto,se obtuvo: "+formato+" y se esperaba .txt")
    else:
        copia=True
else:
    nombreCopia+=".txt"
    copia=True

##SI LOS FORMATOS SON CORRECTOS SE COPIA EL CONTENIDO DEL FICHERO ORIGEN EN EL FICHERO COPIA
if origen and copia and  os.path.isfile (nombreOrigen):
    contenido=""
    with open(nombreOrigen,encoding="utf-8",mode="r") as fo:
        linea = fo.readline()
        while linea:
            contenido+=linea
            linea = fo.readline()
       
    with open(nombreCopia,encoding="utf-8",mode="w") as fc:
        fc.write(contenido)
else:
    print("No se pudo realizar la copia del fichero, uno de los dos ficheros no es de texto o no se ha encontrado")