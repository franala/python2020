import functools

def funcion (op = "+",*args, **kwargs):
    resul = 0
    if (op == "+"):
        resul = functools.reduce(lambda x, y: x + y, args)
        print("El resultado es:",resul)
    else:
        if (op == "*"):
            resul = functools.reduce(lambda x, y: x * y, args)
            print("El resultado es:",resul)
    for kwarg in kwargs:
        print(kwarg,":",kwargs[kwarg])

funcion("*",1,2,3,Nombre="Francisco",Apellido="Alacid",Dirección="Berazategui")
