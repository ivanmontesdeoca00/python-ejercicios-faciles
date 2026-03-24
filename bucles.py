### DEFINICION Y ANALOGIA: El while funciona como un reloj despertador con boton de repeticion: "Mientras no me levante, sigue sonando la alarma"

## La regla de oro de todo While: Tiene un inicio, una variable con valor inicial. Tiene una condicion, una pregunta que debe ser cierta para que el bucle siga y Actualizacion: algo que cambie dentro del bucle para que algun momento la condicion sea falsa.

## ESTRUCTURA BASICA

contador = 20 #Inicio, donde parto a contar

while contador <=5: #Condicion (Es menor o igual a 5?) hasta donde llego
    print(f"Vuelta numero {contador}.")
    contador += 1 #Actualizacion (Sumamos 1 en cada vuelta)
print("Carrera terminada pa")


#break (Freno de emergencia) Sirve para salir del bucle inmediatamente, sin importar si la condicion del while sigue siendo verdadera

while True: #Bucle infinito aproposito
    contador = input("Escribe salir:")
    if contador == 'salir':
        break #rompe el bucle y sale
    print(f"Escribiste: {contador}")
    
    
#Continue: Sirve para ignorar el resto del codigo en la vuelta actual, y saltar directo a la siguiente comparacion del while, se usa para saltar numeros impares o ignorar datos invalidaos sin cerrar el bucle

n = 0
while n <5:
    n+= 1
    if n == 3:
        continue #salta el print del 3 y vuelve arriba
    print(n)
#resultado 1,2,4,5 (el 3 se lo salto)salir


#Control de flujo en bucles: break: rompe el bucle y sale de el, mientras que continue "Salta" el codigo restante de la vuelta actual y va directo a la siguiente comparacion.

