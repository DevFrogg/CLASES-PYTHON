import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    @property
    def diametro(self) -> float:
        return self.radio * 2

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def circunferencia(self) -> float:
        return 2 * math.pi * self.radio

    def __str__(self):
        return (
            f"Círculo — Radio: {self.radio} | Diámetro: {self.diametro} | "
            f"Área: {self.area():.4f} | Circunferencia: {self.circunferencia():.4f}"
        )


# --- Ejemplo de uso ---
if __name__ == "__main__":
    c = Circulo(7)
    print(c)
