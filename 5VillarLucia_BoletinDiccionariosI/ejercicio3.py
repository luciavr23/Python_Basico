#Crea un programa que permita introducir a un profesor las notas de sus estudiantes (máximo 10 estudiantes). 
# Los datos se deberán almacenar en un diccionario como el siguiente:
#estudiantes = 	
# {"1": {"nombre": "Lorena","nota": 8},
#"2": {"nombre": "Markel","nota": "4.2"},
#"3": {"nombre": "Julen","nota": 6.5}}
#Una vez introducidos todos los datos, el programa mostrará una lista con los nombres de los estudiantes que han suspendido 
#y otra con los que han aprobado. También calculará y mostrará la nota media de la clase

contador=1
alumnos={}

def pintaAlumnos(diccionario):
    for alu in diccionario:
        print(f"{alu} : {diccionario[alu]}")

def obtenerCalificaciones(diccionario):
    suma=0
    print("Alumnos Suspensos/Aprobados: ")
    for alu in diccionario:
        alumnoNombre = diccionario[alu][0]
        alumnoNota = diccionario[alu][1]
        if(alumnoNota["nota"]<5):
            print(f"{alumnoNombre['nombre']} --> nota: {alumnoNota['nota']} - Suspenso")
        else:
            print(f"{alumnoNombre['nombre']}--> nota: {alumnoNota['nota']} - Aprobado")
        suma+=alumnoNota["nota"]
    print(f"Nota media de la clase: {round(suma/len(diccionario),2)}")


alumno=input("Introduzca nombre del alumno (0 para salir) :")
while(alumno!="0" and contador<=10):
    alumnoNombre = {"nombre": alumno}
    alumnoNota = {"nota": float(input("Introduzca nota: "))}
    alumnos[contador]=alumnoNombre,alumnoNota
    contador+=1
    if(contador<=10):
        alumno=input("Introduzca nombre del alumno (0 para salir) :")

print(f"Hay {len(alumnos)} alumnos en lista: ")
pintaAlumnos(alumnos)
obtenerCalificaciones(alumnos)
