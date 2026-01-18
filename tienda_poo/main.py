from modelos.tienda import Tienda
from modelos.producto import Producto
from modelos.producto_descuento import ProductoDescuento
from modelos.verdura import Verdura
from servicios.inventario import Inventario

# Crear tienda
tienda = Tienda("Tienda La Económica")
tienda.mostrar_nombre()

# Crear inventario
inventario = Inventario()

# Crear productos
producto_normal = Producto("Arroz", 2.50)
producto_descuento = ProductoDescuento("Azúcar", 1.80)
verdura = Verdura("Lechuga", 0.90, True)

# Agregar productos al inventario
inventario.agregar_producto(producto_normal)
inventario.agregar_producto(producto_descuento)
inventario.agregar_producto(verdura)

# Mostrar inventario
inventario.mostrar_inventario()
