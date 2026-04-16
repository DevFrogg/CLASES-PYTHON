from datetime import datetime

class Coche:
    def __init__(self, marca: str, modelo: str, anio: int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def anios_transcurridos(self) -> int:
        return datetime.now().year - self.anio

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio}) — {self.anios_transcurridos()} años de antigüedad"


# --- Ejemplo de uso ---
if __name__ == "__main__":
    coche = Coche("Toyota", "Corolla", 2015)
    print(coche)
