def funcionA (*args):
    print("Función A:")
    suma = 0
    cant = 0
    for arg in args:
        if(cant<30):
            suma = suma + arg
    print("El resultado de la suma es:",suma)

def funcionB (nombre = "No especifica", apellido = "No especifica", sexo = "No especifica", **kwargs):
    print("Función B:")
    for kwarg in kwargs:
        print(kwarg,":",kwargs.items)

funcionA(1,2,3,4,5,6)
funcionB()
