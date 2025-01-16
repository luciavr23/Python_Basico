#Escribe un programa que pida por teclado siete números enteros positivos y calcule su suma y su multiplicación.
rango = 7
suma = 0
multiplicacion = 1

for i in range(rango):
    numero = int(input("Introduce un número positivo: "))
    while numero < 0:
        numero = int(input("Introduce un número positivo: "))
    suma += numero
    if i == 0:
        multiplicacion = numero
    else:
        multiplicacion *= numero

print("La suma es:", suma)
print("La multiplicación es:", multiplicacion)