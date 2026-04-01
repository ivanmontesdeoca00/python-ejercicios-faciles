palabra = input("Ingresa una palabra: ")

for letra in palabra:
    if letra.lower() in "aeiou":
        continue  
    
    if letra.lower() == "z":
        break  
    
    print(letra)