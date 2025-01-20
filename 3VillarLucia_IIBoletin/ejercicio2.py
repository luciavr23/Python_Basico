#Escribir un programa que a través de un menú permita al usuario sumar, restar, multiplicar o dividir dos operandos. 
# El menú tendrá la opción 5 de salir.
print("Introduzca la opción deseada:")
print("1-Sumar\n2-Restar\n3-Multiplicar\n4-Dividir\n5-Salir")
opcion=int(input("Introduce la opción deseada: "))

def operacion(opcion):
    if opcion == 1:
        return operando1 + operando2
    elif opcion == 2:
        return operando1 - operando2
    elif opcion == 3:
        return operando1 * operando2
    elif opcion == 4:
        return operando1 / operando2
    else:
        return "Opción no válida"

while(opcion!=5):
    operando1=int(input("Introduce el primer operando: "))
    operando2=int(input("Introduce el segundo operando: "))   
    print("Resultado:", operacion(opcion))
    print("\n1-Sumar\n2-Restar\n3-Multiplicar\n4-Dividir\n5-Salir")
    opcion=int(input("Introduce la opción deseada: "))




