for productos in range(1,9):
    respuesta = input(f"El producto {productos} esta vencido? si/no: ").lower()
    if respuesta == "si":
     print("Alerta!! Retirar producto")
    break
else: 
    print("Todo en orden")