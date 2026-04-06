nombre = "esternocleidomastoideo"
busqueda = "o"
encontrado = False
contador = 0

for letra in nombre:
    if letra == busqueda:
        encontrado = True
        contador += 1
        continue #ya lo encontre, no necesito revisar las otras 15 letras
if encontrado:
        print(f"La letra {busqueda} si esta en la palabra, {contador} de veces")
else:
        print(f"No se encontro la letra")