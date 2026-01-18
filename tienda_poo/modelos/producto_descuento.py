from modelos.producto import Producto

# Clase hija que hereda de Producto
class ProductoDescuento(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

    # Polimorfismo: sobrescribe el método
    def calcular_precio_final(self):
        return self.get_precio() * 0.90  # 10% de descuento
