# Escribir un programa que procese una serie de cadenas introducidas por teclado. Sabemos que la carga de datos
# finaliza cuando el usuario introduzca la cadena “0”. 
# Se pide mostrar el total de ocurrencias de cada carácter de todas las cadena procesadas.

cadena=input("Intruduzca una cadena / 0 para salir: ")

abecedario={}
arrayCadenas=[]

while(cadena!="0"):
    arrayCadenas.append(cadena)
    cadena=input("Intruduzca una cadena / 0 para salir: ")

print("Palabras introducidas: " ,arrayCadenas)

for palabra in arrayCadenas:
    for letra in palabra.lower():
        if letra not in abecedario:
            abecedario[letra]=1
        else:
            abecedario[letra]+=1

print("Letras que aparecen: ",abecedario)