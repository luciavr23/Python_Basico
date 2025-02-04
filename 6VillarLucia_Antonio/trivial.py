#El juego consiste en responder preguntas de distintas categorías (ciencia, historia, deportes, entretenimiento, etc.). 
# El jugador recibirá una pregunta y varias opciones de respuesta. Deberá seleccionar la opción correcta para ganar puntos. 
# Al final del juego, se mostrará la puntuación total del jugador.
# Objetivos del Juego
# Responder correctamente a las preguntas de diferentes categorías.
# Acumular la mayor cantidad de puntos posible.
# Permitir al jugador elegir entre diferentes categorías de preguntas(ciencia, historia, deportes, etc.). 
# Sed originales con las categorías y las preguntas. 
# Tiempos de respuesta: Añadir un temporizador para responder cada pregunta. (import time)
# Adicionalmente: Ofrecer preguntas de diferentes niveles de dificultad (fácil, medio, difícil).
import random;

puntos=0
def niveles():
    print("Selecciona un nivel de dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")

preguntasFac = {
    'ciencia': [
        ('¿Cuántos planetas tiene el sistema solar?', ['7', '8', '9', '10'], '8'),
        ('¿De qué color es el sol visto desde la Tierra?', ['Rojo', 'Azul', 'Amarillo', 'Verde'], 'Amarillo'),
        ('¿Qué gas respiramos principalmente?', ['Oxígeno', 'Nitrógeno', 'Hidrógeno', 'Dióxido de carbono'], 'Oxígeno')
    ],
    'historia': [
        ('¿De qué país era Napoleón Bonaparte?', ['España', 'Francia', 'Italia', 'Alemania'], 'Francia'),
        ('¿Cómo se llamaban los barcos de Cristóbal Colón?', ['Pinta, Niña y Santa María', 'Titanic, Mayflower y Beagle', 'Endeavour, Victoria y Bounty', 'Santa Isabel, Pinta y María'], 'Pinta, Niña y Santa María'),
        ('¿En qué año llegó Cristóbal Colón a América?', ['1492', '1600', '1776', '1810'], '1492')
    ],
    'informática': [
        ('¿Cuál es el sistema operativo más usado en ordenadores personales?', ['Linux', 'Windows', 'macOS', 'DOS'], 'Windows'),
        ('¿Qué significa "CPU"?', ['Centro de Procesos Únicos', 'Unidad Central de Procesamiento', 'Computadora Personal Unificada', 'Controlador de Procesos Universales'], 'Unidad Central de Procesamiento'),
        ('¿Qué lenguaje de programación es conocido por su logo de una taza de café?', ['Python', 'C++', 'Java', 'Ruby'], 'Java')
    ]
}

preguntasMed = {
    'ciencia': [
        ('¿Cuál es el elemento químico más abundante en la corteza terrestre?', ['Oxígeno', 'Hierro', 'Silicio', 'Carbono'], 'Oxígeno'),
        ('¿Qué tipo de onda es la luz?', ['Longitudinal', 'Transversal', 'Electromagnética', 'Sonora'], 'Electromagnética'),
        ('¿Qué nombre recibe el cambio de estado de sólido a gas sin pasar por líquido?', ['Condensación', 'Sublimación', 'Evaporación', 'Fusión'], 'Sublimación')
    ],
    'historia': [
        ('¿En qué año terminó la Segunda Guerra Mundial?', ['1939', '1945', '1918', '1960'], '1945'),
        ('¿Qué civilización construyó Machu Picchu?', ['Aztecas', 'Mayas', 'Incas', 'Egipcios'], 'Incas'),
        ('¿Quién fue el líder de la Revolución Rusa de 1917?', ['Lenin', 'Stalin', 'Trotsky', 'Marx'], 'Lenin')
    ],
    'informática': [
        ('¿Qué significa HTML?', ['Hyper Transfer Markup Language', 'Hyper Text Markup Language', 'High Tech Modern Language', 'Hyperlink and Text Management Language'], 'Hyper Text Markup Language'),
        ('¿Cuál de estos lenguajes es de tipado estático?', ['Python', 'JavaScript', 'Java', 'Ruby'], 'Java'),
        ('¿Cuál es el protocolo principal para transferir páginas web?', ['FTP', 'HTTP', 'SMTP', 'SSH'], 'HTTP')
    ]
}

preguntasDif = {
    'ciencia': [
        ('¿Quién propuso la teoría de la relatividad general?', ['Isaac Newton', 'Albert Einstein', 'Niels Bohr', 'Galileo Galilei'], 'Albert Einstein'),
        ('¿Qué es la antimateria?', ['Materia sin electrones', 'Materia compuesta de partículas opuestas a las de la materia normal', 'Materia invisible', 'Materia compuesta de partículas iguales a las de la materia normal'], 'Materia compuesta de partículas opuestas a las de la materia normal'),
        ('¿Qué es la quiralidad en química?', ['Un tipo de reacción', 'La simetría de las moléculas', 'Un fenómeno en la interacción de electrones', 'El fenómeno donde dos estructuras no pueden superponerse en el espacio'], 'El fenómeno donde dos estructuras no pueden superponerse en el espacio')
    ],
    'historia': [
        ('¿En qué batalla murió Napoleón Bonaparte?', ['Batalla de Waterloo', 'Batalla de Leipzig', 'Batalla de Austerlitz', 'Batalla de Trafalgar'], 'Batalla de Waterloo'),
        ('¿Qué imperio fue derrotado por los musulmanes en la batalla de Poitiers en 732?', ['Imperio Romano', 'Imperio Bizantino', 'Imperio Carolingio', 'Imperio Visigodo'], 'Imperio Carolingio'),
        ('¿Quién fue el autor de la teoría del materialismo histórico?', ['Karl Marx', 'Friedrich Engels', 'Max Weber', 'Emile Durkheim'], 'Karl Marx')
    ],
    'informática': [
        ('¿Cuál es la principal diferencia entre un algoritmo de búsqueda binaria y un algoritmo de búsqueda lineal?', ['El binario requiere una lista ordenada, mientras que el lineal no', 'El binario es más rápido sin importar la estructura de datos', 'El binario funciona solo en listas de cadenas, el lineal en listas numéricas', 'No hay diferencia significativa entre ambos'], 'El binario requiere una lista ordenada, mientras que el lineal no'),
        ('¿Qué es un buffer overflow?', ['Un tipo de error de programación en el que se excede la capacidad de memoria reservada', 'Una técnica para encriptar datos', 'Un protocolo de transferencia de archivos', 'Un proceso para optimizar bases de datos'], 'Un tipo de error de programación en el que se excede la capacidad de memoria reservada'),
        ('¿Qué es la "recursión" en programación?', ['Cuando una función se llama a sí misma', 'Un tipo de algoritmo iterativo', 'Una técnica para evitar el uso de variables', 'Un error de programación'], 'Cuando una función se llama a sí misma')
    ]
}

print("Bienvenido al trivial.")
niveles()
respuesta=int(input("Introduce el número del nivel: "))
if respuesta ==1: 
    print("Has seleccionado el nivel fácil.")
    categoria=random.choice(list(preguntasFac.keys()))
    print("La categoría seleccionada es: ",categoria)
    pregunta=random.choice(preguntasFac[categoria])
    print(pregunta[0])
    print("Opciones: ",pregunta[1])
    respuesta=input("Introduce tu respuesta: ")
    if(respuesta==pregunta[2]):
        print("Respuesta correcta")
        puntos+=1
elif respuesta==2:
    print("Has seleccionado el nivel medio.")
    categoria=random.choice(list(preguntasMed.keys()))
    print("La categoría seleccionada es: ",categoria)
    pregunta=random.choice(preguntasFac[categoria])
    print(pregunta[0])
    print("Opciones: ",pregunta[1])
    respuesta=input("Introduce tu respuesta: ")
    if(respuesta==pregunta[2]):
        print("Respuesta correcta")
        puntos+=1
else: 
    print("Has seleccionado el nivel dificil.")
    categoria=random.choice(list(preguntasDif.keys()))
    print("La categoría seleccionada es: ",categoria)
    pregunta=random.choice(preguntasFac[categoria])
    print(pregunta[0])
    print("Opciones: ",pregunta[1])
    respuesta=input("Introduce tu respuesta: ")
    if(respuesta==pregunta[2]):
        print("Respuesta correcta")
        puntos+=1
