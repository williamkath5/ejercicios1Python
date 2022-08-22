# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a
# intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por
# el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y
# tercer año. Redondear cada cantidad a dos decimales.

print("Sistema para calcular la suma de los ahorros del CDT")
print("_____________________________________________________")

cantidad = int(input("Ingrese la cantidad a ahorrar en el CDT: "))
tiempo = int(input("Ingrese el tiempo del ahorro en años:"))
interes = float(input("Ingresa el porcentaje de ganancia al año: "))

interesAnio = cantidad*interes/100
ganancia = interesAnio*tiempo

print("El valor a ahorrar en el CDT es de ", cantidad, " pesos MCTE", "\nEl tiempo del CDT es de ", tiempo, " años", "\nEl valor del interés es del ", interes, "%", "\nLa ganancia total es de ", ganancia, " Pesos MCTE", "\nTotal a recibir: ", cantidad+ganancia)