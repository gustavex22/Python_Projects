import random 

Numero = random.randint(1, 100) 

print("__Adivina el numero!!___")

Numero_user = input("Se ha generado un numero entre 1 y 100  adivina cual es: ")

if Numero_user == Numero :
        print("Ganaste!!!")
        
else:
    print(f"Perdiste!! El numero era: {Numero}")