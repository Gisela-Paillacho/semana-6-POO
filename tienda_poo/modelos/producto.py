# Clase base Producto
class Producto:
    def __init__(self, nombre, precio):
        # Atributos encapsulados (privados)
        self.__nombre = nombre
        self.__precio = precio

    # Métodos getters (encapsulación)
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    # Método que será sobrescrito (polimorfismo)
    def calcular_precio_final(self):
        return self.__precio
