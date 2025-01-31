#Modifica el ejercicio anterior para que el programa informe del número de ocurrencias de las distintas letras del alfabeto
#  incluyendo aquellas que no aparezcan (indicar valor 0)

abecedario={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,
            "m":0,"n":0,"ñ":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,
            "x":0,"y":0,"z":0}

cadena=input("Intruduzca una cadena / 0 para salir: ")
arrayCadenas=[]
            
#funcion que recorra los char de cada cadena, los cuente y los meta en un diccionario como clave valor
while(cadena!="0"):
    arrayCadenas.append(cadena)
    cadena=input("Intruduzca una cadena / 0 para salir: ")

for letra in abecedario:
    for palabra in arrayCadenas:
        for char in palabra.lower():
            if letra==char:
                abecedario[letra]+=1

print("Abecedario:",abecedario)