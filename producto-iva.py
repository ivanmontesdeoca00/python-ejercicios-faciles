producto = input("Ingrese el nombre de su producto: ")

cantidad = int(input("Seleccione la cantidad de producto: "))

precio_unidad = float(input("Ingrese el precio del producto que desea: "))

precio_total = cantidad * precio_unidad

#Imprime el precio total

iva = precio_total * 0.19

precio_total_iva = iva + precio_total

print(f"El precio total sin iva es de ${precio_total}")

print(f"El precio total CON IVA es de ${precio_total_iva}")

