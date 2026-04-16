class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aumentar_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        self.stock += cantidad
        print(f"Stock aumentado. Stock actual de '{self.nombre}': {self.stock}")

    def disminuir_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        if cantidad > self.stock:
            raise ValueError(f"Stock insuficiente. Disponible: {self.stock}")
        self.stock -= cantidad
        print(f"Stock reducido. Stock actual de '{self.nombre}': {self.stock}")

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}"


# --- Ejemplo de uso ---
if __name__ == "__main__":
    p = Producto("Auriculares", 49.99, 100)
    print(p)
    p.aumentar_stock(20)
    p.disminuir_stock(15)
    print(p)
