with open("ñ.txt",encoding="utf-8",mode="r") as f:
    print("leer fichero:")
    print(f.read())
    f.seek(0)
    print("1º linea:")
    print(f.readline(),end="")
    f.seek(0)
    print("leer todas las lineas:")
    print(f.readlines())
    print("leer linea a linea mediante bucle:")
    f.seek(0)
    for linea in f:
        print(linea,end="")

#f.read(): lee todo el archivo y deja el puntero al final.
#f.readline(): .devuelve 1 linea . Si el puntero ya está al final, devuelve una cadena vacía.
#f.readlines(): Devuelve una lista de lineas.También devuelve una lista vacía si el puntero está al final.
#for linea in f: Imprime linea a linea. No imprime nada si el puntero esta al final.
# f.seek(0): se utiliza para mover el puntero por el archivo, en este caso lo coloca al principio.
#lastIndexO= nombreOrigen.rfind(".") busca el index del "."