class Te:
    precio_300gr = 3000
    precio_500gr = 5000

    @staticmethod
    def obtener_tiempo_recomendacion(sabor):
        if sabor == 1:
            return 3, "Consumir al desayuno"
        elif sabor == 2:
            return 5, "Consumir al medio día"
        elif sabor == 3:
            return 6, "Consumir al atardecer"
        
    @staticmethod
    def obtener_precio(formato):
        if formato == 300:
            return Te.precio_300gr
        elif formato == 500:
            return Te.precio_500gr