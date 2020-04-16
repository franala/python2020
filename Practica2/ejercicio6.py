num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

op = input("""
        Elija la operacion:

    suma: +
    resta: -
    multiplicacion: *
    division: /

    """)

while (op != '+' and op != '-' and op != '*' and op != '/'):
    op = input("Operacion no valida, intente de nuevo: ")

if (op == '+'):
    print("Resultado: ", (num1 + num2))
else:
    if (op == '-'):
        print("Resultado: ", (num1 - num2))
    else:
        if (op == '*'):
            print("Resultado: ", (num1 * num2))
        else:
            print ("Resultado: ", (num1 / num2))
