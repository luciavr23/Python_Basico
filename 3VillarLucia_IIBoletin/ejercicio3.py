#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****

altura=int(input("Introduce la altura del triángulo (entero positivo): "))
if(altura>0):
    for i in range(1,altura+1):
        print("*"*i)    