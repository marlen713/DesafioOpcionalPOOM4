
from te import Te

sabor = int(input("Ingrese el número correspondiente al sabor (1: Té negro, 2: Té verde, 3: Agua de hierbas): "))
formato = int(input("Ingrese el formato deseado (300 o 500 gr): "))

te_pedido = Te()
tiempo, recomendacion = te_pedido.obtener_tiempo_recomendacion(sabor)
precio = te_pedido.obtener_precio(formato)

print("Detalle del pedido:")
print("Sabor del té:", {1: "Té negro", 2: "Té verde", 3: "Agua de hierbas"}[sabor])
print("Formato:", formato, "gr")
print("Precio: $", precio)
print("Tiempo de preparación:", tiempo, "minutos")
print("Recomendación:", recomendacion)