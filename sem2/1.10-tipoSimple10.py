# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo
# y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos
# y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
# programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del
# paquete que será enviado.
print("\nSistema de cálculo del peso de envíos de la juguetería")
print("__________________________________________________________")

payaso = 112
muneca = 75

cantPayasos = int(input("Ingrese la cantidad de payasos: "))
cantMunecas = int(input("Ingrese la cantidad de muñecas: "))
pedPayaso = cantPayasos*payaso
pedMunecas = cantMunecas*muneca

total = pedPayaso+pedMunecas

print("\nLa cantidad de payasos seleccionada es de: ", cantPayasos, "\nLa cantidad de muñecas seleccionada es de: ", cantMunecas, "\nEl peso de los payasos es de: ", pedPayaso, "Gr", "\nEl peso de las muñecas es de: ", pedMunecas, "Gr" "\nEl peso total es de: ", total, "Gramos")