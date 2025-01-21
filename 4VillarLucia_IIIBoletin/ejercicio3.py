#Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), 
# y posterior ordene los elementos de menor a mayor.
import random

lista=[10]
for i in range(10):
    lista.append(random.randint(1,10))
lista.sort()
print("Lista ordenada de menor a mayor: ",lista)