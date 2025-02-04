#Escribir una función, obtenerNumerosArchivo, que reciba por parámetro el nombre de un archivo que almacenará una serie de cantidades 
# enteras y positivas (un número por línea). La función leerá todos los valores del archivo, calculará su suma y la devolverá.
import os
def obtenerNumerosArchivo(nombre):
    if(os.path.isfile (nombreOrigen))
nombreArchivo=input("Indica el nombre del archivo que desea leer: ")
if("." in nombreArchivo):
    formato = nombreArchivo[".":]
else:
    nombreArchivo+=".txt"
if(formato!=".txt"):
    print("El archivo no es de texto,se obtuvo: "+formato+" y se esperaba .txt")
else:
    obtenerNumerosArchivo(nombreArchivo)


