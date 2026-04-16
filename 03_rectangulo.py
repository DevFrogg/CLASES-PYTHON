class Rectangulo:
    def __init__(self, longitud: float, anchura: float):
        self.longitud = longitud
        self.anchura = anchura

    def area(self) -> float:
        return self.longitud * self.anchura

    def perimetro(self) -> float:
        return 2 * (self.longitud + self.anchura)

    def __str__(self):
        return (
            f"Rectángulo {self.longitud}x{self.anchura} — "
            f"Área: {self.area():.2f} | Perímetro: {self.perimetro():.2f}"
        )


# --- Ejemplo de uso ---
if __name__ == "__main__":
    r = Rectangulo(8, 5)
    print(r)
