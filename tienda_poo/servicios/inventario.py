class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        print("\nInventario de la tienda:")
        for p in self.productos:
            print(f"- {p.get_nombre()} | Precio final: ${p.calcular_precio_final():.2f}")
