#Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
#La temperatura media de cada día
#Los días con menos temperatura
#Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. 
# si no existe ningún día se muestra un mensaje de información.
tempMinimas=[5]
tempMaximas=[5]


#REPASAR#
def tempMin(temperaturas):
    minima=min(tempMinimas)
    print(f"El día con menor temperatura registrada es: {temperaturas.index(minima)+1} con un valor de {minima:.2f}ºC")

#REPASAR#
def buscaTemp(temperaturas):
    inputTemp=float(input("Introduzca temperatura máxima a buscar: "))
    if inputTemp in temperaturas:
        diasRegistrados=[]
        for i, temp in enumerate(tempMaximas):  
            if temp == inputTemp:
                diasRegistrados.append(i + 1)  
        print(f"La temperatura máxima de {inputTemp}ºC se ha registrado en los días: {diasRegistrados}")
    else:
        print("No se ha registrado ninguna temperatura máxima con ese valor")


for i in range(5):
    min=float(input(f"Introduzca temperatura mínima para el día {i+1}: "))
    max=float(input(f"Introduzca temperatura máxima para el día {i+1}: "))
    tempMinimas.append(min)
    tempMaximas.append(max)

for i in range(5):
    media=(tempMinimas[i]+tempMaximas[i])/2
    print(f"La temperatura media del día {i+1} es: {media:.2f}ºC")

tempMin(tempMinimas)
buscaTemp(tempMaximas)
