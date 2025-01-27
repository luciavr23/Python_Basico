def menu():
    print("-----MENÚ-----")
    print("1- Mostrar la lista")
    print("2- Insertar un Alumno en la lista")
    print("3- Eliminar un Alumno de la lista")
    print("4- Crear una copia de la lista alumnos")
    print("5- Añadir un alumno a la lista copia")
    print("6- Crear lista de pesos")
    print("7- Mostrar lista de pesos")
    print("8- Mostrar personas con más de 100kg")
    print("9- Salir")

def solicitaAlumnos():
    for i in range(5):
        alumno=input("Introduzca nombre del alumno:")
        listaAlumnos.append(alumno)
        
def insertaAlumno(lista):
    alumnoNuevo=input("Introduce el nombre del alumno a insertar:")
    if(alumnoNuevo not in lista):
        lista.append(alumnoNuevo)
    else:
        print("El alumno ya está en la lista.")

def masDe100():
    contador=0
    for i in range(len(listaPesos)):
        if(listaPesos[i]>100):
            print(f"Persona {i+1} con un peso de: {listaPesos[i]}")
            contador+=1
    print(f"Hay {contador} que pesan más de 100 kg")

listaAlumnos=[]
listaAlumnosCopia=[]
listaPesos=[]

solicitaAlumnos()
menu()
opcion=int(input("Selecciona una opción: "))
while(opcion!=9):
    if(opcion==1):
        print("Lista de alumnos:",listaAlumnos)
    elif(opcion==2):
        insertaAlumno(listaAlumnos)
    elif(opcion==3):
        alumnoEliminar=input("Inttroduzca alumno a eliminar:")
        if(alumnoEliminar in listaAlumnos):
            listaAlumnos.remove(alumnoEliminar)
    elif(opcion==4):
        listaAlumnosCopia=listaAlumnos.copy()
    elif(opcion==5):
        insertaAlumno(listaAlumnosCopia)
        print("Lista original:",listaAlumnos)
        print("Lista copia:",listaAlumnosCopia)
    elif(opcion==6):
        listaPesos=[53.2, 141.8, 105.3, 78.2, 60.4]
        print("Lista creada")
    elif(opcion==7):
        print("Lista de pesos:",listaPesos)
        print("Peso mínimo:",min(listaPesos))
        print("Peso máximo:",max(listaPesos))
        print("Media de peso:",(sum(listaPesos)/len(listaPesos)))
    elif(opcion==8):
        masDe100()
    else:
        print("Opción no válida")
    menu()
    opcion=int(input("Selecciona una opción: "))


