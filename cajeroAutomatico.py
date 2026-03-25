saldo = 5000

while True:
    print("\n1. Ver saldo")
    print("2. salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo}")
    elif opcion == "2":
        print ("Saliendo del sistema")
        break
    else:
        print("Opcion no valida.")