

capacidad_maxima = 1000 
capacidad_actual = 0  
contador_paquetes = 0  

""" Lista de 6 paquetes (peso, estado, alarma)
# estado: "ok" o "roto"
# alarma: True o False"""
paquetes = [
    {"peso": 20, "estado": "ok", "alarma": False},
    {"peso": 30, "estado": "roto", "alarma": False},
    {"peso": 25, "estado": "ok", "alarma": False},
    {"peso": 40, "estado": "ok", "alarma": False},  
    {"peso": 10, "estado": "ok", "alarma": False},
    {"peso": 100, "estado": "ok", "alarma": True} #Emergencia
]

for paquete in paquetes:
    contador_paquetes += 1
    print(f"\nInspeccionando paquete {contador_paquetes}")

    
    if paquete["alarma"]:
        print(" ALARMA DE INCENDIO, SE CORTA TODO.")
        break

    
    if paquete["estado"] == "roto":
        print(" PAQUETE ROTO, A LA BASURA. ")
        continue

    
    if capacidad_actual + paquete["peso"] > capacidad_maxima:
        print("CAPACIDAD MAXIMA ALCANZADA, NO ENTRA MAS")
        break

   
    capacidad_actual += paquete["peso"]
    print(f"PAQUETE CARGADO: Peso: {paquete['peso']}")
    print(f"CAPACIDAD ACTUAL: {capacidad_actual}/{capacidad_maxima}")

print("\n--- RESUMEN ---")
print(f"Paquetes procesados: {contador_paquetes}")
print(f"Capacidad final: {capacidad_actual}/{capacidad_maxima}")