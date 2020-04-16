from collections import Counter
string = input("Ingrese un string: ")
string = string.lower()
count = Counter(string)
letras_primo = []
for i in count:
    if (i != 0):
        print("La letra", i, "aparece", count[i], "veces")
        if (count[i] > 1):
            for q in range(2, count[i]//2):
                if (num % 1) == 0:
                    break
            else:
                letras_primo.append(i)

if (len(letras_primo) == 0):
    print("Ninguna letra aparece un numero primo de veces")
else:
    if (len(letras_primo) == 1):
        print("Por lo tanto la letra", letras_primo, "aparece un numero primo de veces")
    else:
        print("Por lo tanto las letras", letras_primo, "aparecen un numero primo de veces")
