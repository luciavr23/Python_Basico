#Diseñar el programa que:
#Cree una tabla (lista con dos dimensiones) de 5x5 enteros.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.
import random

matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(random.randint(1, 100))
    matriz.append(fila)

for i in range(5):
    suma = 0
    for j in range(5):
        suma += matriz[i][j]
    print(f"La suma de la fila {i+1} es: {suma}")

for i in range(5):
    suma = 0
    for j in range(5):
        suma += matriz[j][i]
    print(f"La suma de la columna {j+1} es: {suma}")
    
    
