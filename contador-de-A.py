palabra = input("Ingresa una palabra: ").lower()
cuenta_a = 0

for letra in palabra:
    if letra == "a":
        cuenta_a += 1
        if cuenta_a == 3:
            print("Limite de A alcanzazdo. Abortando....")
            break
    else: 
        print(letra)


        
