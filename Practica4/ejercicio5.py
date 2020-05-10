import PySimpleGUI as sg
import json

def modificoDatos (datos_jugador):
    with open("archivoEj5.txt", 'r') as arch:
        dic_datos = json.load(arch)
    with open("archivoEj5.txt", 'w') as arch:
        if datos_jugador[0] in dic_datos:
            print("Existe")
            print(dic_datos)
        else:
            print("Agrego nuevo")
            print(dic_datos)
        dic_datos[datos_jugador[0]] = {}
        dic_datos[datos_jugador[0]]['nivel'] = int(datos_jugador[1])
        dic_datos[datos_jugador[0]]['puntaje'] = int(datos_jugador[2])
        dic_datos[datos_jugador[0]]['tiempo'] = int(datos_jugador[3])
        print(dic_datos)
        json.dump(dic_datos,arch, indent=4)

datos = {
    'fede': { 'nivel': 3, 'puntaje': 4, 'tiempo': 200 },
    'belen': { 'nivel': 5, 'puntaje': 10, 'tiempo': 400 },
    'juan': { 'nivel': 15, 'puntaje': 110, 'tiempo': 400 },
    'pedro': { 'nivel': 5, 'puntaje': 3, 'tiempo': 400 }
}

archivo = open("archivoEj5.txt","w")
json.dump(datos,archivo,indent=4)
archivo.close()
#archivo = open("archivoEj5.txt","r+")

layout = [
    [sg.Text('Nombre:', size=(15,1)), sg.InputText()],
    [sg.Text('Nivel:', size=(15,1)), sg.InputText()],
    [sg.Text('Puntaje:', size=(15,1)), sg.InputText()],
    [sg.Text('Tiempo:', size=(15,1)), sg.InputText()],
    [sg.Button('Guardar'), sg.Button('Cancelar')]
]

window = sg.Window("Ventana").Layout(layout)

event, values = window.Read()

if event in (None, 'Cancelar'):
    window.Close()
else:
    window.Close()
    modificoDatos(values)
    #archivo.close()
    layout = [
        [sg.Text('El jugador fue guardado exitosamente')],
        [sg.Button('Aceptar')]
    ]
    window = sg.Window("Ventana").Layout(layout)
    event = window.Read()
