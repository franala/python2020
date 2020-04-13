rawList = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']

lower = []
greater = []

print("Ingrese un numero: ")

number = input()

for i in rawList:
    name, space, tupla = i.partition(" ")
    x = int(tupla.split(",")[0])
    if x > int(number):
        greater.extend([name, tupla])
    else:
        lower.extend([name, tupla])

print(greater)
print(lower)    
