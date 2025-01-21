#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
notas=[]


def media(notas):
    print("Media de la evaluación:",sum(notas)/len(notas))

def notaMaxima(notas):
    print("Nota máxima:", max(notas))

def notaMin(notas):
    print ("Nota mínima",min(notas))

for i in range(5):
    nota=int(input("Introduce una nota: "))
    notas.append(nota)

for examen in notas:
    print(f"Nota del examen: {examen}")

media(notas)
notaMaxima(notas)
notaMin(notas)
