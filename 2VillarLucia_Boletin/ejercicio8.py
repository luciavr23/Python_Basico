#Solicitar un número y ver si es primo o no. 
numero=int(input("Introduce un número: "))
noEsPrimo=False

for i in range(2,10):
    if noEsPrimo==True:
        break
    if numero%i==0 and i!=numero:
        noEsPrimo=True
if noEsPrimo==False and numero>1 and numero%numero==0 and numero%1==0:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")