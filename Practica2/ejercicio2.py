rawList = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134']
newList = []

for i in rawList:
    name, space, tupla = i.partition(" ")
    x, _, y = tupla.partition(",")
    newList.append( (int(x), int(y)) )

print(newList)
newList.sort()
print(newList)
