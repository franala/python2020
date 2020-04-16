string = input("Ingrese un string: ")
string = string.lower()
if (string == string[::-1]):
    print("Es palindromo")
else:
    print("No es palindromo")
