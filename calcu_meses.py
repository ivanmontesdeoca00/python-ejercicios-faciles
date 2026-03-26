meses = int(input("Ingrese el mes que desea en numero 1-12: "))

if meses >= 1 and meses <=4:
    print("Estas en la estacion de Verano")
elif meses >= 5 and meses <= 8:
    print("Estas en la estacion de Invierno")
elif meses >= 9 and meses <= 11:
    print("Estas en la estacion de primavera")
elif meses == 12:
    print("Estas en la estacion de otoño")
else: print("Error: ingresa bien el mes del año ura")