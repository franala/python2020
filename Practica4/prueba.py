import PySimpleGUI as sg

layout = [
    [sg.Text('Sarasa')],
]

window = sg.Window("Ventana").Layout(layout)

while True:
    event, values = window.Read()
    print(f"Evento: {event}")

    if event in (None, 'Exit'):
        break

window.close()
