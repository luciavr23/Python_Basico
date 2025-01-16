#Nuevo sueldo. Calcular si un empleado aumenta su sueldo. Para ello solicitaremos dos valores enteros: sueldo y antigüedad. 
    #Si el sueldo es <500 y tiene más de 10 años de antigüedad tendrá el triple de su sueldo. 
    #Si el sueldo es <500 y tiene menos de 10 años de antigüedad tendrá el doble de su sueldo. 
    #En cc se queda con el mismo sueldo. 
sueldo= int(input("Introduce tu sueldo: "))
antiguedad= int(input("Introduce tu antigüedad: "))
if sueldo < 500 and antiguedad > 10:
    sueldo *= 3
    print(f"Tu nuevo sueldo es de {sueldo}")
elif sueldo < 500 and antiguedad < 10:
    sueldo*=2
    print(f"Tu nuevo sueldo es de {sueldo}")
else: 
    print("Tu sueldo no cambia")