frase = input("Escriba una frase: ")
sub = input("Escriba un string: ")
print(frase.split())
lista = frase.lower()
frase = frase.split()
lista = lista.split()
sub = sub.lower()
cont = 0
for x in lista:
  if sub in x:
    print(x)
    cont = cont + 1

print("Veces que aparece el string: " + str(cont))

nuevo_str = (" ".join(x for x in lista))
nuevo_str = nuevo_str.upper()
print("String nuevo: " + nuevo_str)
