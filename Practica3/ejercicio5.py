import random

def estructura1 (colores,coordenadas):
    dic = dict()
    for i in coordenadas:
        dic[i] = random.choice(colores)
    return dic

def estructura2 (colores, coordenadas):
    random.shuffle(colores)
    dic = dict(zip(coordenadas,colores))
    return dic

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]

print (estructura1(colores,coordenadas))
print (estructura2(colores,coordenadas))
