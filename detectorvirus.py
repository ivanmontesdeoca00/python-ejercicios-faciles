archivos = ["a","b","c","x","e","f"]

print(" --- Iniciando escaneo del sistema ---")
for archivo in archivos:
    if archivo == "x":
        print ("Peligro virus detectado X, Bloqueando el sistema...")
        break
    print(f"Procesando archivo {archivo}... OK")
    print("--- FIN DEL REPORTE- ---")