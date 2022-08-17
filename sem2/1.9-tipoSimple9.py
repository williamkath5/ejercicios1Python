# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión.

print("\nSistema para saber cuánto me debe la rata Eliana")
print("_______________________________________________")

cantidad = int(input("Ingresa el monto del préstamo: "))
interes = float(input("Ingresa el interés mensual del préstamo: "))
cantAnios = int(input("Ingresa el tiempo del préstamo en años: "))

valorTotInt = cantidad*interes/100
anual = valorTotInt*12
total = (anual*cantAnios)+cantidad

print("El monto solicitado es de: ", cantidad, "\nLa tasa de interés mensual es de: ", interes, "%", "\nEl valor del interés mensual es de: ", valorTotInt, "\nEl tiempo del préstamo es de: ", cantAnios, " años", "\nEl interés anual es de: ", anual, "\nEl ingreso total es de: ", total)