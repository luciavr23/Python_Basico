#Carga desde teclado la información de los pacientes de un determinado hospital perteneciente a una aseguradora 
# privada. 
#Sabemos que a través del dni del paciente queremos tener acceso a: nombre, edad, si ha sido atendido previamente 
# en ese hospital y al código (valor numérico entero) de su médico de cabecera.
#- Visualiza la información almacenada.
#- Calcula la edad media de todos los pacientes que han sido atendidos alguna vez en ese hospital.
#- Visualiza el listado de todos los pacientes de un determinado médico cuyo código se solicitará por teclado.
pacientes={
    "29503322A":{"nombre":"Lucia", "edad":24, "atendido":True, "medico":1},
    "29503323B":{"nombre":"Luis", "edad":34, "atendido":True, "medico":2}
}

def menu():
    print("---Menú---")
    print("1. Añadir paciente")
    print("2. Visualizar pacientes")
    print("3. Calcular la edad media de pacientes atendidos")
    print("4. Visualizar pacientes de un médico determinado")
    print("5. Salir")

def pintaPacientes(diccionario):
    for paciente in diccionario:
        print(f"{paciente} : {diccionario[paciente]}")

def calculaEdadMedia(diccionario):
    suma=0
    for paciente in diccionario:
        if(diccionario[paciente]["atendido"]==True):
            suma+=diccionario[paciente]["edad"]
    print("La edad media entre los pacientes atendidos es de: ",round(suma/len(diccionario),2)) 

menu()
opcion=int(input("Selecciona una opción: "))
while(opcion!=5):
    if(opcion==1):
        dni=input("Introduce dni del paciente: ")
        nombre=input("Introduce nombre del paciente: ")
        edad=int(input("Introduce edad del paciente: "))
        atendido=bool(input("Introduce si ha sido atendido previamente en el hospital: "))
        medico=int(input("Introduce código del médico de cabecera: "))
        pacientes[dni]={"nombre":nombre, "edad":edad, "atendido":atendido, "medico":medico}
        print("Paciente añadido correctamente")
    elif(opcion==2):
        pintaPacientes(pacientes)
    elif(opcion==3):
        calculaEdadMedia(pacientes)
    elif(opcion==4):
        codMedico=int(input("Introduzca código del médico a consultar:"))
        for paciente in pacientes:
            if(pacientes[paciente]["medico"]==codMedico):
                print(f"Paciente: DNI-{paciente}, Nombre:{pacientes[paciente]['nombre']}")
    else:
        print("Opción no válida") 
    menu()
    opcion=int(input("Selecciona una opción: "))
    
