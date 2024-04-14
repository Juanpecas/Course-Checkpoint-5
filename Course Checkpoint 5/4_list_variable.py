nombre = 'Enrique'

lista_nombre = ('Jessica', 'Paul', 'George', 'Henry', 'Adán')

encontrado = False

for nombre_en_lista in lista_nombre:
    if nombre_en_lista == nombre:
        encontrado = True
        break

if encontrado:
    print(f"{nombre} esta en la lista")
else:
    print(f"{nombre} no esta en la lista")

    

