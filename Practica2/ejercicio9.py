import random

intentos = 0

print("Hola! ¿Cual es tu nombre?")
miNombre = input()

numero = random.randint(1,50)
print("Bueno, " + miNombre + ", estoy pensando un numero entre 1 y 50")

for intentos in range(6):
    print("Adivina.")
    adiv = input()
    adiv = int(adiv)

    if adiv < numero:
        print("Muy bajo")

    if adiv > numero:
        print("Muy alto")

    if intentos == 3:
        if (numero % 2 == 0):
            print("El numero es par")
        else:
            print("El numero es impar")

    if adiv == numero:
        break

if adiv == numero:
    intentos = str(intentos + 1)
    print("Bien, " + miNombre + "! Adivinaste mi numero en " + intentos + " intentos")

if adiv != numero:
    numero = str(numero)
    print("Perdiste, el numero que estaba pensado era " + numero + ".")
