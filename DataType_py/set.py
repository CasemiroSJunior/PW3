lista3 = []
for x in range(10):
    lista3.append(x)
    lista3.append(x +1)

listaTemp = []
for n in lista3:
    if n not in listaTemp:
        listaTemp.append(n)

lista3 = listaTemp

print(lista3)

lista4 = []
for x in range(10):
    lista4.append(x)
    lista4.append(x +1)

lista4 = list(set(lista4))
print(lista4)