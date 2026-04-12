print("--- SISTEMA DE GASOLINERA ---")

for bomba in range(1, 4):
    print(f"\nRevisando bomba {bomba}...")
    respuesta = input(f"Bomba {bomba}: ¿Desea cargar combustible? (si o no): ").lower()

    if respuesta == "no":
        print("Bueno, que tenga buenas tardes.")
        continue

    if respuesta == "si":
        monto = float(input("Ingrese el monto a cargar: "))

        while monto <= 0:
            monto = float(input("Error, ingrese un monto válido: "))

        print(f"Bomba {bomba} cargada con ${monto}")

print("\n--- MUCHAS GRACIAS POR SU COMPRA ----")