# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
# coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

print("Bienvenido al sistema de cálculo de honorarios")
cantidadHoras = int(input("\nIngrese la cantidad de horas trabajadas: "))
costeHora = int(input("\nIngrese el valor por hora: "))

valorAPagar = cantidadHoras*costeHora

print("El valor a pagar es de",valorAPagar)