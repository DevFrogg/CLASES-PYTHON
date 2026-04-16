import math

class Banco:
    def __init__(self, nombre: str, tasa_interes: float):
        """
        :param nombre: Nombre del banco.
        :param tasa_interes: Tasa de interés anual en porcentaje (ej: 5 para 5%).
        """
        self.nombre = nombre
        self.tasa_interes = tasa_interes / 100  # convertir a decimal

    def calcular_interes(self, capital: float, anios: int) -> float:
        """Interés compuesto generado tras 'anios' años."""
        monto_final = capital * (1 + self.tasa_interes) ** anios
        return monto_final - capital

    def anios_para_duplicar(self, capital: float) -> float:
        """Años necesarios para duplicar el capital (regla del logaritmo)."""
        if self.tasa_interes <= 0:
            raise ValueError("La tasa de interés debe ser mayor que 0.")
        return math.log(2) / math.log(1 + self.tasa_interes)

    def __str__(self):
        return f"Banco: {self.nombre} | Tasa de interés: {self.tasa_interes * 100:.2f}%"


# --- Ejemplo de uso ---
if __name__ == "__main__":
    banco = Banco("Banco Nacional", 5)
    print(banco)
    capital = 10_000
    anios = 10
    interes = banco.calcular_interes(capital, anios)
    print(f"Interés generado en {anios} años sobre ${capital:,}: ${interes:,.2f}")
    print(f"Años para duplicar ${capital:,}: {banco.anios_para_duplicar(capital):.2f} años")
