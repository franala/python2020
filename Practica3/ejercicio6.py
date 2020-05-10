import random

def func1():
    x = int(input("Ingrese el primer numero:"))
    y = int(input("Ingrese el segundo numero:"))
    print("El resultado de la suma es:", x + y)

def func2
    num = random.randrange(3)
    palabras = [('grave',['molesto']), ('aguda',['ratón']),('esdrujula',['murciélago'])]
    print('De acuerdo a su acentuacion, a que categoria corresponde la palabra '+(palabras[num][1][0])+'?')
    respuesta = input()
    if(respuesta == (palabras[num][0])):
        print("Su respuesta es correcta")
    else:
        print("Su respuesta es incorrecta")

def estructura (colores,coordenadas):
    dic = dict()
    for i in coordenadas:
        dic[i] = random.choice(colores)
    return dic

colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
dicFunc = {'azul': func1, 'amarillo': func2, 'rojo': func1, 'blanco': func2, 'negro': func1}

print(coordenadas)
dic = estructura(colores,coordenadas)
print(dic)
x = int(input("Ingrese coordenada X:"))
y = int(input("Ingrese coordenada Y:"))
while ((x,y) not in coordenadas):
    print("Esas coordenadas no existen, ingrese nuevamente")
    x = int(input("Ingrese coordenada X:"))
    y = int(input("Ingrese coordenada Y:"))

dicFunc[dic[x,y]]()
