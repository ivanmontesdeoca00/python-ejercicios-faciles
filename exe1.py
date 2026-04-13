"""
1. El Validador de Inventario
Tienes una lista de tuplas donde cada tupla contiene (nombre_producto, cantidad, precio).

Tarea: Crea un programa que recorra la lista y genere un diccionario.

Condición: Si la cantidad es menor a 5, agrégalo al diccionario con la clave "Reposición Crítica". Si es mayor o igual a 5, agrégalo a la clave "Stock Ok".

Extra: Al final, muestra cuántos productos hay en cada categoría."""

# Datos de entrada: (nombre_producto, cantidad, precio)
productos = [
    ("Manzanas", 10, 1.5),
    ("Pera", 3, 2.0),
    ("Naranjas", 2, 1.2),
    ("Bananas", 15, 0.8),
    ("Kiwi", 1, 3.5)
]

# Inicializamos el diccionario con las dos categorías requeridas
inventario_clasificado = {
    "Reposición Crítica": [],
    "Stock Ok": []
}

# Recorremos la lista de tuplas
for nombre, cantidad, precio in productos:
    # Evaluamos la condición de la cantidad
    if cantidad < 5:
        inventario_clasificado["Reposición Crítica"].append(nombre)
    else:
        inventario_clasificado["Stock Ok"].append(nombre)

# --- Salida de resultados ---

print("Estado del Inventario:")
print(f"Críticos: {inventario_clasificado['Reposición Crítica']}")
print(f"Suficientes: {inventario_clasificado['Stock Ok']}")

print("-" * 20)

# Extra: Mostrar cuántos productos hay en cada categoría
for categoria, lista_productos in inventario_clasificado.items():
    cantidad_total = len(lista_productos)
    print(f"En la categoría '{categoria}' hay {cantidad_total} productos.")