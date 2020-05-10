import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json

def main(args):

	sigo_jugando = True
	while sigo_jugando:

		layout = [
			[sg.Text('Nombre de jugador:'), sg.InputText()],
			[sg.Text('Elegí con qué juego querés jugar:')],
			[sg.Button('Ahorcado'), sg.Button('Ta-Te-Ti')],[sg.Button('Otello')],
			[sg.Button('Salir')]
			]

		window = sg.Window("Ventana").Layout(layout)

		event, values = window.Read()
		window.Close()
		if (event != 'Salir'):
			with open("archivoJugadores.txt","a") as archivo:
				dic = {'Jugador': values[0], 'Juego:': event}
				json.dump(dic,archivo, indent=4)

		if event == 'Ahorcado':
			hangman.main()
		elif event == 'Ta-Te-Ti':
			tictactoeModificado.main()
		elif event == 'Otello':
			reversegam.main()
		elif event == 'Salir':
			sigo_jugando = False

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
