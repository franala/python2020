rawList = ['Auto', '123', 'Viaje', '50', '120']
newList = []

for i in rawList:
    if i.isdecimal():
        newList.append( i )

print(newList)
