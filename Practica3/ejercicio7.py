jugadores = {
    'fede': { 'nivel': 3, 'puntaje': 4, 'tiempo': 200 },
    'belen': { 'nivel': 5, 'puntaje': 10, 'tiempo': 400 },
    'juan': { 'nivel': 15, 'puntaje': 110, 'tiempo': 400 },
    'pedro': { 'nivel': 5, 'puntaje': 3, 'tiempo': 400 }
}

for i in jugadores.keys():

	print("Puntaje del jugador",jugadores(i),":",jugadores[i]["puntaje"])
	print(" ")

listaOrdenadaPorNombre = sorted(jugadores.items(), key=lambda jugador: jugadores.items)

print(listaOrdenadaPorNombre)
print(" ")

listaOrdenadaPorNivel = sorted(jugadores.items(), key=lambda jugador: jugador[1][1])

print(listaOrdenadaPorNivel)
print(" ")
