#Programa que pida números hasta que se introduzca el 0. Debe calcular la suma y la media de los números introducidos.
print("Introduzca 0 para salir")
numero=int(input("Introduce un número mayor que 0: "))
suma=0
contador=0

while(numero!=0):
    suma+=numero
    contador+=1
    numero=int(input("Introduce un número mayor que 0: "))
media=suma/contador
print("La suma de los números introducidos es: ",suma)
print(f"La media de los números introducidos es: {media:.2f}")    