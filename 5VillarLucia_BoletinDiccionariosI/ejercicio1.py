# Escribir un programa que procese una serie de cadenas introducidas por teclado. Sabemos que la carga de datos
# finaliza cuando el usuario introduzca la cadena “0”. 
# Se pide mostrar el total de ocurrencias de cada carácter de todas las cadena procesadas.

cadena=input("Intruduzca una cadena / 0 para salir: ")

abecedario={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"ñ":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
arrayCadenas=[]
#funcion que recorra los char de cada cadena, los cuente y los meta en un diccionario como clave valor
while(cadena!="0"):
    arrayCadenas.append(cadena)
    ocurrencias(arrayCadenas)
    cadena=input("Intruduzca una cadena / 0 para salir: ")