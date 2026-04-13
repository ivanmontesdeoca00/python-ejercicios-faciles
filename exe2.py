"""2. Filtro de Usuarios por Edad
Crea un programa que reciba una lista de diccionarios, donde cada diccionario tiene los datos de un usuario: {"nombre": str, "edad": int, "ciudad": str}.

Tarea: Utilizando un ciclo y condicionales, separa a los usuarios en dos listas nuevas: una para los que viven en "Córdoba" y son mayores de 18 años, y otra para el resto.

Salida: Imprime solo los nombres de los usuarios que cumplieron la condición de Córdoba."""

# Lista de diccionarios con datos de usuarios
usuarios = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Córdoba"},
    {"nombre": "Pedro", "edad": 15, "ciudad": "Córdoba"},
    {"nombre": "Juan", "edad": 30, "ciudad": "Rosario"},
    {"nombre": "María", "edad": 22, "ciudad": "Córdoba"},
    {"nombre": "Luis", "edad": 18, "ciudad": "Mendoza"},
    {"nombre": "Sofía", "edad": 19, "ciudad": "Córdoba"}
]

# Listas para separar los resultados
cordobeses_mayores = []
otros_usuarios = []

# Recorremos la lista de diccionarios
for usuario in usuarios:
    if usuario["ciudad"] == "Córdoba" and usuario["edad"] > 18:
        cordobeses_mayores.append(usuario)
    else:
        otros_usuarios.append(usuario)



print("Usuarios de Córdoba mayores de 18 años:")
# Recorremos la lista filtrada
for u in cordobeses_mayores:
    print(f"- {u['nombre']}")

print("-" * 30)
print(f"Total en Córdoba: {len(cordobeses_mayores)}")
print(f"Total en el resto del grupo: {len(otros_usuarios)}")