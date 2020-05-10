diccionario = {}

for i in range(10):

	nombre = input("Ingrese nombre del jugador: ")
	print(" ")
	nivel = int(input("Nivel alcanzado: "))
	print(" ")
	puntaje = int(input("Puntaje maximo: "))
	print(" ")
	tiempo = int(input("Tiempo de juego: "))
	print(" ")

	lista = [nombre,nivel,puntaje,tiempo]

	diccionario[nombre] = lista

print(diccionario)
print(" ")

for i in diccionario:

	print("Puntaje del jugador",diccionario[i][0],":",diccionario[i][2])
	print(" ")

listaOrdenadaPorNombre = sorted(diccionario.items(), key=lambda jugador: jugador[1][0])

print(listaOrdenadaPorNombre)
print(" ")

listaOrdenadaPorNivel = sorted(diccionario.items(), key=lambda jugador: jugador[1][1])

print(listaOrdenadaPorNivel)
print(" ")
