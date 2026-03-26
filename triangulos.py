A = int(input("Ingrese su valor en Grados del L1: "))
B = int(input("Ingrese su valor en grados del L2: "))
C = int(input("Ingrese su valor en grados del L3: "))


if A + B + C != 180:
    print("Datos incorrectos. La suma debe ser 180°.")
else:
    if A == B == C:
        print("Este triángulo es Equilátero.")
    elif A == B or B == C or A == C:
        print("Este triángulo es Isósceles.")
    else:
        print("Este triángulo es Escaleno.")