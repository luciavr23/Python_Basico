# Escribir un programa que procese una serie de cadenas introducidas por teclado. Sabemos que la carga de datos
# finaliza cuando el usuario introduzca la cadena “0”. 
# Se pide mostrar el total de ocurrencias de cada carácter de todas las cadena procesadas.

cadena=input("Intruduzca una cadena / 0 para salir: ")

arrayCadenas=[]
#funcion que recorra los char de cada cadena, los cuente y los meta en un diccionario como clave valor
while(cadena!="0"):
    arrayCadenas.append(cadena)
    ocurrencias(arrayCadenas)
    cadena=input("Intruduzca una cadena / 0 para salir: ")