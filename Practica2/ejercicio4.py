import random

preguntas = [
    ['Buenos Aires limita con Santiago del Estero', 'no'],
    ['Jujuy limita con Bolivia', 'si'],
    ['San Juan limita con Misiones', 'no']
]

puntaje = 0
aux = 0
total = len(preguntas)

for i in range(total):
    indice = random.randrange(0, len(preguntas))
    print(preguntas[indice][0])

    respuesta = input()

    if preguntas[indice][1].lower() == respuesta.lower():
        puntaje = puntaje + 1
    else:
        print("Incorrecto")

    del preguntas[indice]

print("Respuestas correctas: " + str(puntaje))
