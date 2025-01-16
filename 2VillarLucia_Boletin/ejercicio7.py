#Solicitar una nota (float) y mostrar mensaje: 
    #Si nota < 3: “muy deficiente”
    #Si nota < 5: “insuficiente”
    #Si nota < 6: “suficiente”
    #Si nota < 7:”bien”
    #Si nota < 9: “notable”
    #Si nota <10: “sobresaliente”
nota=float(input("Introduce tu nota: "))

if nota < 3:
    print("Muy deficiente")
elif nota < 5:
    print("Insuficiente")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")