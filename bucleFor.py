"""
El for se usa para iterar (recorrer) los elementos de una secuencia. Una secuencia puede ser una lista de numeros, un string o un rango determinado.
analogia del tren: Imagina un tren con varios vagones, el bucle for es un revisor que entra al primer vagon, hace algo, luego pasa al segundo y asi sucesivamente.    
    
"""

## Estructura basica

## Sintaxis: for (inicializacion;condicion;actualizacion):
## for elemento in secuencia:
## instrucciones
"""
nombres = ["ana", "luis","juan"]

for nombre in nombres:
    print(f"Hola {nombre}")
    
"""

""" Inicializacion: se ejecuta UNA SOLA VEZ al principio. Normalmente sirve para declarar e inicializar una variable de control (contador, ) por ejemplo: let i= 0
Condicion: se evalua antes de cada iteracion. Si es True el codigo dentro del bucle se ejecuta; si es false el bucle termina, por ejemplo: i < 10
Actualizacion: se ejecuta al final de cada vuelta para modificar la variable de contro por ejemplo: i++ (incrementando) o i--(decremento)
Componentes claves: Cuerpo del bucle, osea las intrucciones que quieres repetir. Variables de control: la variable que rastrea en que opaso del ciclo te encuentras. Y Paso o Step: la cantidad en la que aumenta o disminuye la variable de control en cada vuelta"""

## El aliado inseparable: RANGE()

"""Como se trabajo con muchos numeros usamos el range(inicio,fin,salto)
range(5)----> Genera numeros del 0 al 4.
range(1,6)-----> Genera numeros del 1 al 5"""

## Contador de numeros

"""numero = int(input("De que numero quieres la tabla?: "))

print(f'--- TABLA DEL {numero} ---')
for i in range(1,11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')"""
    
    
##Contador de vocales

frase = input("Escriba una frase mi rey: ").lower()
contador_a = 0

for letra in frase:
    if letra == "a":
        contador_a += 1
print(f'La letra +a+ aparece {contador_a} veces.' )