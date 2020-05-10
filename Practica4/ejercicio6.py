import json
from pattern.es import parse, conjugate, INFINITIVE

dic_verbos = {}

with open("archivoEj6Texto.txt","r") as arch:
    for line in arch:
        lista = parse(line).split()
        print(lista)
        for pal in lista:
            print(pal)
            if ('VB' in pal):
                dic_verbos[conjugate(pal,INFINITIVE)] = {}
                dic_verbos[palabra]['cantidad'] += 1

print(dic_verbos)
