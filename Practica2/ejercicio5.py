import time

def menu ():
    print("""\n Menu de opciones para la lista de números a ingresar:

    1: ingresar numeros
    2: ordenar numeros
    3: calcular el maximo
    4: calcular el minimo
    5: calcular el promedio
    0: para terminar \n""")

def validar (opcion):
    while (opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 0):
        opcion = int(input("Esa opcion no es valida, ingrese otro numero: "))
    return opcion


menu()
opcion = int(input("Opcion: "))
lista = []
while (validar(opcion) != 0):
    if (opcion == 1):
        num = int(input("\nIngrese el numero: "))
        lista.append(num)
    if (opcion == 2):
        if not lista:
            print("La lista esta vacia")
        else:
            print("\nSin ordenar:\n", lista)
            lista.sort()
            print("\nOrdenado:\n", lista)
    if (opcion == 3):
        if not lista:
            print("La lista esta vacia")
        else:
            print("\nEl maximo es: ", max(lista))
    if (opcion == 4):
        if not lista:
            print("La lista esta vacia")
        else:
            print("\nEl minimo es: ", min(lista))
    if (opcion == 5):
        if not lista:
            print("La lista esta vacia")
        else:
            print("\nEl promedio es: ", (sum(lista)/len(lista)))
    time.sleep(1)
    menu()
    opcion = int(input("Opcion: "))
