#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla 
# cada elemento de la lista junto con su cuadrado y su cubo.
import random

lista=[10]

for i in range(10):
    lista.append(random.randint(1,10))
    print(f"Posición {i}: El cuadrado de ",lista[i]," es ",lista[i]**2," y su cubo es ",lista[i]**3)

