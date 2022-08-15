#Ejemplo 2: Energía cinética de cuerpos rígidos

#Es posible determinar la energía cinética de un cuerpo mediante diversas fórmulas en la mecánica clásica
#Función input() obtiene información
#Función float() transforma lo recibido en número real

masa=float(input("Registre la masa: "))
velocidad=float(input("Registre la velocidad del cuerpo: "))

EC=masa*(velocidad**2)*(1/2)
print("\nEnergía cinética=",EC, "Juls")