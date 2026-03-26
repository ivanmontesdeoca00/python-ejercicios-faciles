control_velocidad = int(input("Ingrese la velocidad de su auto registrada: "))

if control_velocidad <= 20:
    print("Su velocidad es muy lenta")
elif control_velocidad >20 and control_velocidad <= 60:
    print("Su velocidad es moderada")
elif control_velocidad >= 61 and control_velocidad <= 120:
    print("Su velocidad es alta")
elif control_velocidad > 121:
    print("¡¡¡Multa por exceso de velocidad!!!")
else: print ("Ingrese bien su velocidad")
