class Tienda:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._productos: list[str] = []

    def añadir_producto(self, producto: str):
        self._productos.append(producto)
        print(f"'{producto}' añadido a {self.nombre}.")

    def eliminar_producto(self, producto: str):
        if producto not in self._productos:
            raise ValueError(f"'{producto}' no está en el inventario.")
        self._productos.remove(producto)
        print(f"'{producto}' eliminado de {self.nombre}.")

    def listar_productos(self) -> list[str]:
        return list(self._productos)

    def __str__(self):
        productos = ", ".join(self._productos) if self._productos else "sin productos"
        return f"Tienda: {self.nombre} | Productos: {productos}"


# --- Ejemplo de uso ---
if __name__ == "__main__":
    tienda = Tienda("El Mercado")
    tienda.añadir_producto("Manzanas")
    tienda.añadir_producto("Pan")
    tienda.añadir_producto("Leche")
    print(tienda)
    tienda.eliminar_producto("Pan")
    print("Lista de productos:", tienda.listar_productos())
