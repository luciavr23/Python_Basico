#Escribe un programa que pida por teclado siete números enteros y calcule su suma y su multiplicación.
suma=0
multiplicacion=0
for i in range(7):
    numero=int(input("Introduce un número: "))
    suma+=numero
    if i==0:
        multiplicacion=numero
    else:
        multiplicacion*=numero

print(f"La suma de los números es: {suma}")
print(f"La multiplicación de los números es: {multiplicacion}")