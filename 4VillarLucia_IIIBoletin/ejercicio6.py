#Crear un programa que añada números a una lista hasta que introducimos un número negativo. 
# A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. 
# Muestra esta segunda lista para comprobar que hemos eliminado los duplicados.
lista=[]
num=int(input("Introduzca un número positivo (numero negativo para salir): "))

while num>=0:
    lista.append(num)
    num=int(input("Introduzca un número positivo (numero negativo para salir): "))

listaSinDuplicados=[]

for i in lista:
    if listaSinDuplicados.count(i)==0:
        listaSinDuplicados.append(i)

print("Lista original:",lista)
print("Lista sin duplicados:",listaSinDuplicados)