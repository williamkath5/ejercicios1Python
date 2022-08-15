# Variables numéricas con input

nombre=input("Por favor ingresa tu nombre: ")

altura=float(input("Por favor ingresa tu altura: "))
masa=int(input("Por favor ingresa tu masa: "))

IMC=masa/(altura**2)
print(nombre, "Tu índice de masa corporal es de ", IMC)