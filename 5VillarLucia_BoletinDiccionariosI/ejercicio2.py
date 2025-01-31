#Modifica el ejercicio anterior para que el programa informe del número de ocurrencias de las distintas letras del alfabeto
#  incluyendo aquellas que no aparezcan (indicar valor 0)

abecedario={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,
            "m":0,"n":0,"ñ":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,
            "x":0,"y":0,"z":0}

arrayCadenas=[]

#funcion que pinta el diccionario con un valor debajo de otro
def pintaAbecedario(diccionario):
    for letra in diccionario:
        print(f"{letra} : {diccionario[letra]}")
        #para pintar los valores seguidos print(abecedario)

#funcion que cuenta las veces que aparece cada letra del abecedario en el array de palabras
def cuentaConcurrencias(diccionario,array):
    for letra in diccionario:
        for palabra in array:
            for char in palabra.lower():
                if letra==char:
                    diccionario[letra]+=1

#inicializar array
cadena=input("Introduzca una cadena ( 0 para salir ) : ")
while(cadena!="0"):
    arrayCadenas.append(cadena)
    cadena=input("Introduzca una cadena ( 0 para salir ) : ")

#hago una llamada a las funciones definidas
cuentaConcurrencias(abecedario,arrayCadenas)
pintaAbecedario(abecedario)