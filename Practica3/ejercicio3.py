jugadores = {
    'fede': { 'nivel': 3, 'puntaje': 4, 'tiempo': 200 },
    'belen': { 'nivel': 5, 'puntaje': 10, 'tiempo': 400 },
    'juan': { 'nivel': 15, 'puntaje': 110, 'tiempo': 400 },
    'pedro': { 'nivel': 5, 'puntaje': 3, 'tiempo': 400 }
}

print("\nEstructura original: \n", jugadores)

print("\nSolo nombres: \n", jugadores.keys())

print("\nJugador con mayor puntaje:\n", max(jugadores.items(), key=lambda jugador:jugador[1]['puntaje'] ))

print("\nNueva jugada:\n")
nombre_jugador = input("Ingrese nombre del Jugador de la jugada: ")
puntaje_jugada = input(f"Ingrese puntaje de la jugada de {nombre_jugador}: ")
nivel_jugada = input(f"Ingrese nivel de la jugada de {nombre_jugador}: ")
tiempo_jugada = input(f"Ingrese tiempo de la jugada de {nombre_jugador}: ")
juga_nuevo = {'nivel': nivel_jugada, 'puntaje': puntaje_jugada, 'tiempo': tiempo_jugada}
jugadores.setdefault(nombre_jugador,juga_nuevo)
print("\nJugadores actualizados:\n", jugadores)

print("\nMejores 10 jugadores:\n")
jugadores_or = sorted(jugadores.items(),
                      key=lambda punt: punt[1]['puntaje'],reverse=True)
jugadores_or[:10]
