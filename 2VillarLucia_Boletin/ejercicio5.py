#Solicitar tres números por teclado y comprobar si alguno de ellos es mayor que 10. Mensaje:”Alguno de los 3 números es mayor que 10”
num1=int(input("Introduce el primer número: "))
num2=int(input("Introduce el segundo número: "))
num3=int(input("Introduce el tercer número: "))
if num1>10 or num2>10 or num3>10:
    print("Alguno de los 3 números es mayor que 10")
else:
    print("Ninguno de los 3 números es mayor que 10")