passport = input("Tu pasaporte esta vigente? (Si/No): ").lower().strip()
if passport == "no":
    print("No podes ingresar al pais. Tenes que dirigirte a la oficina de tramites.")
elif passport == "si":
    print("\nMotivos de viaje: turismo, trabajo, estudio")
    motivo = input("Cual es el motivo de su viaje: ").lower().strip()
    if motivo == "turismo":
        print("Motivo autorizado por 90 dias.")
    elif motivo == "trabajo":
        print("Debe presentar su contrato laboral en el modulo 5")
    elif motivo == "estudio":
        print("Debe mostrar su comprobante de matricula")
    else:
        print("Porfavor, espere a un oficial de migraciones.")
else:
    print("Respuesta incorrecta. Por favor reinicie el proceso y responda 'Si' o 'No'. ")
    