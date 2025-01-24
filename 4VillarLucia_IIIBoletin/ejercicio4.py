#Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
#La temperatura media de cada día
#Los días con menos temperatura
#Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. 
# si no existe ningún día se muestra un mensaje de información.
tempMinimas=[]
tempMaximas=[]

for i in range(5):
    minTemp=float(input(f"Introduzca temperatura mínima para el día {i+1}: "))
    maxTemp=float(input(f"Introduzca temperatura máxima para el día {i+1}: "))
    tempMinimas.append(minTemp)
    tempMaximas.append(maxTemp)

for i in range(5):
    media=(tempMinimas[i]+tempMaximas[i])/2
    print(f"La temperatura media del día {i+1} es: {media:.2f}ºC")

#REPASAR#
def tempMin(temperaturas):
    minima=min(temperaturas)
    print("Días con temperatura mínima registrada:")
    for i in range(5):
        if temperaturas[i] == minima:
            print(f"Día {i} con un valor de {minima:.1f}ºC")
    

#REPASAR#
def buscaTemp(temperaturas):
    inputTemp=float(input("Introduzca temperatura máxima a buscar: "))
    print(f"Días con temperatura máxima de {inputTemp}ºC")
    enc=False
    for i in range (5):
        if inputTemp == temperaturas[i]:
            print(f"Día {i+1}")
            enc=True
    if enc==False:
        print("No se ha registrado ninguna temperatura máxima con ese valor")

tempMin(tempMinimas)
buscaTemp(tempMaximas)
