#Escriba un programa que permita crear una lista de palabras y que, a continuación de las siguientes opciones:
#Contar: Me pide una cadena, y me cuantas veces aparece en la lista
#Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones de la primera por la 
# segunda en la lista.
#Eliminar: Me pide una cadena, y la elimina de la lista.
#Mostrar: Muestra la lista de cadenas
#Terminar

def menu(palabrasArray):
    if opcion==1:
        cadena=input("Introduzca una cadena): ")
        print(f"La cadena {cadena} aparece {palabrasArray.count(cadena)} veces en la lista")
    elif opcion==2:
        cadena=input("Introduzca cadena a modificar: ")
        cadenaModificada=input("Introduzca la cadena modificada: ")
        enc=False
        for i in range(len(palabrasArray)):
            if palabrasArray[i]==cadena:
                palabrasArray[i]=cadenaModificada
                enc=True
        if enc==True:
            print("Cadena modificada")
        else:
            print("Cadena no encontrada")
    elif opcion==3:
        cadena=input("Introduzca una cadena): ")
        enc=False
        for i in range(len(palabrasArray)):
            if palabrasArray[i]==cadena:
                palabrasArray.remove(cadena)
                enc=True
        if enc==True:
            print("Cadena eliminada")
        else:
            print("Cadena no encontrada")
    else:
        print(palabrasArray)

palabras=[]

crearLista=input("Introduzca una palabra (f para finalizar): ")

while crearLista!="f":
    palabras.append(crearLista)
    crearLista=input("Introduzca una palabra (f para finalizar): ")

print("1- Contar, 2- Modificar, 3- Eliminar, 4- Mostrar, 5- Terminar")
opcion=int(input("Introduzca una opción): "))

while opcion!=5:
    menu(palabras)
    print("1- Contar, 2- Modificar, 3- Eliminar, 4- Mostrar, 5- Terminar")
    opcion=int(input("Introduzca una opción): "))
    