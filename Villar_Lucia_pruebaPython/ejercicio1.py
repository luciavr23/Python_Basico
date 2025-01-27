
listaAlumnos=[]
listaAlCopia=[]
listaPesos=[]

def solicitaAlumnos():
    for i in range(5):
        alumno=input("Inserta nombre del Alumno:")
        listaAlumnos.append(alumno)
    print("Lista creada")

def listar(lista):
    for i in range(len(lista)):
        print(f"Alumno {i+1} : {lista[i]}")

def eliminaAlu(lista):
    alumno=input("Inserta nombre del Alumno a eliminar")
    enc=False
    for i in range(len(lista)):
        if enc == False and alumno == lista[i]:
            lista.remove(alumno)
            print("Alumno eliminado")
            enc=True
    listar(lista)

def copyListaAlumnos():
    #for i in range(len(listaAlumnos)):
     #   listaAlCopia.append(listaAlumnos[i])
    listaAlCopia=listaAlumnos.copy()

def anadeAlumno(lista):
    alumnoNuevo=input("Inserta nombre del Alumno a insertar:")
    if(alumnoNuevo not in lista):
        lista.append(alumnoNuevo)
        print("Se ha añadido el nuevo alumno")
    else:
        print("El alumno ya existe")

def crearListaPesos(listaPesos):
    listaPesos= [53.2, 141.8, 105.3, 78.2, 60.4]
    print("Lista creada")

def muestraPesos():
    minima=min(listaPesos)
    maxima=max(listaPesos)
    for i in range(len(listaPesos)):
        print(f"Peso {i}:",listaPesos)
    print("Peso mínimo:",minima)
    print("Peso máximo:",maxima)
    print("La media de pesos es:", sum(listaPesos)/len(listaPesos))

def masDe100():
    contador=0
    for i in range(listaPesos):
        if listaPesos[i] >100.0:
            print(f"Peso {i} con un valor de {listaPesos[i]}")
            contador+=1
    print(f"Hay {contador} personas que pesan más de 100 kg")

def menu(opcion):
    if opcion==1:
        listar(listaAlumnos)
    elif opcion==2:
        anadeAlumno(listaAlumnos)
    elif opcion==3:
        eliminaAlu(listaAlumnos)
    elif opcion==4:
        copyListaAlumnos()
    elif opcion==5:
        anadeAlumno(listaAlCopia)
        print("Lista original: ",listaAlumnos)
        print("Lista copia: ",listaAlCopia)
    elif opcion==6:
        crearListaPesos(listaPesos)
    elif opcion==7:
        muestraPesos()
    else:
        masDe100()

solicitaAlumnos()
opcion=int(input("1-Listar Alumnos\n2-Insertar Alumno\n3-Eliminar alumno\n4-Copiar lista\n5-Añadir alumno a lista copiada\n6-Crear lista pesos\n7-Mostrar lista pesos\n8-Personas de mas de 100kg\n9-Salir"))
while(opcion!=9 and opcion>0 and opcion<10):
    menu(opcion)
    opcion=int(input("1-Listar Alumnos\n2-Insertar Alumno\n3-Eliminar alumno\n4-Copiar lista\n5-Añadir alumno a lista copiada\n6-Crear lista pesos\n7-Mostrar lista pesos\n8-Personas de mas de 100kg\n9-Salir"))