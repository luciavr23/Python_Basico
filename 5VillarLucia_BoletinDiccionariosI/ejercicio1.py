# Escribir un programa que procese una serie de cadenas introducidas por teclado. Sabemos que la carga de datos
# finaliza cuando el usuario introduzca la cadena “0”. 
# Se pide mostrar el total de ocurrencias de cada carácter de todas las cadena procesadas.

abecedario={}
arrayCadenas=[]

#funcion que cuenta las veces que salen las letras de las palabras y las mete en el diccionario 
    #!!solo las que aparezcan en las palabras del array
def cuentaConcurrencias(diccionario,array):
    for palabra in array:
        for letra in palabra.lower():
            if letra not in diccionario:
                diccionario[letra]=1
            else:
                diccionario[letra]+=1

#funcion que pinta las letras del diccionario una debajo de otra
def pintaConcurrencias(diccionario):
    for letra in diccionario:
        print(f"{letra} : {diccionario[letra]}")

#inicializar array
cadena=input("Introduzca una cadena / 0 para salir: ")
while(cadena!="0"):
    arrayCadenas.append(cadena)
    cadena=input("Introduzca una cadena / 0 para salir: ")

print("Palabras introducidas: " ,arrayCadenas)
cuentaConcurrencias(abecedario,arrayCadenas)
pintaConcurrencias(abecedario)