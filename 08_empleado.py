class Empleado:
    def __init__(self, nombre: str, edad: int, salario_mensual: float, cargo: str):
        self._nombre = nombre
        self._edad = edad
        self._salario_mensual = salario_mensual
        self._cargo = cargo

    # --- Getters ---
    def get_nombre(self): return self._nombre
    def get_edad(self): return self._edad
    def get_salario(self): return self._salario_mensual
    def get_cargo(self): return self._cargo

    # --- Setters ---
    def set_nombre(self, nombre: str): self._nombre = nombre
    def set_edad(self, edad: int):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = edad
    def set_salario(self, salario: float):
        if salario < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salario_mensual = salario
    def set_cargo(self, cargo: str): self._cargo = cargo

    def salario_anual(self) -> float:
        return self._salario_mensual * 12

    def __str__(self):
        return (
            f"Empleado: {self._nombre} | Edad: {self._edad} | "
            f"Cargo: {self._cargo} | Salario mensual: ${self._salario_mensual:,.2f}"
        )


# --- Ejemplo de uso ---
if __name__ == "__main__":
    emp = Empleado("Carlos", 35, 3500, "Desarrollador Senior")
    print(emp)
    print(f"Salario anual: ${emp.salario_anual():,.2f}")
    emp.set_salario(4000)
    print(f"Nuevo salario mensual: ${emp.get_salario():,.2f}")
