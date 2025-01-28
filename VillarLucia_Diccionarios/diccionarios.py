def menu():
    print("\n1- Listar todas las claves y sus valores")
    print("2- Añadir un nuevo par clave-valor")
    print("3- Eliminar una clave y valor asociado")
    print("4- Buscar el valor de una clave específica")
    print("5- Listar todas las claves del diccionario.")
    print("6- Listar todos los valores del diccionario.")
    print("7- Listar todos los pares clave-valor del diccionario.")
    print("8- Comprobar si una clave existe en el diccionario.")
    print("9- Calcular la suma de todos los valores del diccionario.")
    print("10- Obtener la clave máxima y mínima del diccionario.")
    print("11- Obtener el número total de elementos en el diccionario.\n")

estaturasAlumnos={}


menu()
opcion=int(input("Selecciona una opción: "))
while(opcion!=12):
    if(opcion==1):
        print(estaturasAlumnos)
    elif(opcion==2):
        inputClave=input("Introduce nombre del estudiante:")
        inputValor=float(input("Introduzca la estatura:"))
        estaturasAlumnos[inputClave]=inputValor
    elif(opcion==3):
        inputClave=input("Introduce nombre del estudiante a eliminar:")
        if(inputClave in estaturasAlumnos):
            del estaturasAlumnos[inputClave]
            print("Alumno eliminado")
        else:
            print("La clave no existe")
    elif(opcion==4):
        inputClave=input("Introduce nombre del estudiante a buscar:")
        print("Estatura consultada: ",estaturasAlumnos.get(inputClave,"Alumno no encontrado"))
    elif(opcion==5):
        print(estaturasAlumnos.keys())
    elif(opcion==6):
        print(estaturasAlumnos.values())
    elif(opcion==7):
        print(estaturasAlumnos.items())
    elif(opcion==8):
        inputClave=input("Introduce nombre del estudiante a buscar:")
        print("¿Existe el alumno especificado?", inputClave in estaturasAlumnos)
    elif(opcion==9):
       print("La suma de todas las estaturas es: ",sum(estaturasAlumnos.values()))
    elif(opcion==10):
        print("La clave mínima es: ",max(estaturasAlumnos))
        print("La clave máxima es: ",min(estaturasAlumnos))
    elif(opcion==11):
        print("Elementos encontrados: ",len(estaturasAlumnos))
    else:
        print("Opción no válida")
    menu()
    opcion=int(input("Selecciona una opción: "))
