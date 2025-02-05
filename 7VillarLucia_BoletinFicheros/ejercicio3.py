#Escribir una función, obtenerNumerosArchivo, que reciba por parámetro el nombre de un archivo que almacenará una
#serie de cantidades enteras y positivas (un número por línea). La función leerá todos los valores del archivo, 
#calculará su suma y la devolverá.
import os

def obtenerNumerosArchivo(nombre):
    suma=0
    if(os.path.isfile (nombre)):
        with open(nombre,mode="r") as f:
            num = f.readline()
            while num:
                num=int(num)
                if(num>0):
                    suma+=int(num)
                num = f.readline()
    return suma

formato=""   
nombreArchivo=input("Indica el nombre del archivo que desea leer: ")

punto=nombreArchivo.rfind(".")

if(punto==-1):
    formato=".txt"
    nombreArchivo+=formato
    print(nombreArchivo)
else:
    formato =nombreArchivo[punto:]

if(formato!=".txt"):
    print("El archivo no es de texto,se obtuvo: "+formato+" y se esperaba .txt")
else:
    print(f"La suma del contenido del fichero es: {obtenerNumerosArchivo(nombreArchivo)}")


