from modelos.producto import Producto

# Clase hija Verdura
class Verdura(Producto):
    def __init__(self, nombre, precio, organica):
        super().__init__(nombre, precio)
        self.organica = organica

    # Polimorfismo: implementación propia
    def calcular_precio_final(self):
        if self.organica:
            return self.get_precio() * 1.05  # 5% adicional si es orgánica
        return self.get_precio()
