#Idem al anterior pero definiendo una función
def exponente():
    """
    Esta función recibe una base y exponente y devuelve
    su resultado.
    """
    base=float(input("Introduce la base: "))
    exponente=int(input("Introduce el exponente: "))
    return base**exponente

# Llamamos a la función 
resultado = exponente()
print(f'El resultado de la base elevada al exponente es: {resultado:.2f}')