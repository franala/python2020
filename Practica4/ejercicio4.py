import PySimpleGUI as sg
from datetime import datetime
import json

layout = [
    [sg.Text('Temperatura:', size=(15,1)), sg.InputText()],
    [sg.Text('Humedad:', size=(15,1)), sg.InputText()],
    [sg.Button('Aceptar'), sg.Button('Cancelar')]
]

window = sg.Window("Ventana").Layout(layout)

event, values = window.Read()

if event in (None, 'Cancelar'):
    window.Close()
else:
    f_h = str(datetime.now())
    layout = [
        [sg.Text('Temperatura: ' + values[0])],
        [sg.Text('Humedad: ' + values[1])],
        [sg.Text('Fecha y hora: ' + f_h)],
        [sg.Text('Desea exportar esta información a un archivo?')],
        [sg.Button('Aceptar'), sg.Button('Cancelar')]
    ]

    window = sg.Window("Ventana").Layout(layout)

    event = window.Read()

    if event in (None, 'Cancelar'):
        window.Close()
    else:
        dic = {"Temperatura": values[0], "Humedad": values[1], "Fecha y hora:": f_h}
        archivo = open('archivoEj4.txt','w')
        json.dump((str(dic)), archivo)
        archivo.close()
        window.Close()
