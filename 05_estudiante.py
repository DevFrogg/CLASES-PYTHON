class Estudiante:
    def __init__(self, nombre: str, edad: int, carrera: str):
        self._nombre = nombre
        self._edad = edad
        self._carrera = carrera

    # --- Getters ---
    def get_nombre(self): return self._nombre
    def get_edad(self): return self._edad
    def get_carrera(self): return self._carrera

    # --- Setters ---
    def set_nombre(self, nombre: str): self._nombre = nombre
    def set_edad(self, edad: int):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = edad
    def set_carrera(self, carrera: str): self._carrera = carrera

    def nota_media(self, examenes: list[float]) -> float:
        if not examenes:
            raise ValueError("La lista de exámenes está vacía.")
        return sum(examenes) / len(examenes)

    def __str__(self):
        return f"Estudiante: {self._nombre} | Edad: {self._edad} | Carrera: {self._carrera}"


# --- Ejemplo de uso ---
if __name__ == "__main__":
    e = Estudiante("Laura", 21, "Ingeniería Informática")
    print(e)
    notas = [8.5, 7.0, 9.0, 6.5, 8.0]
    print(f"Nota media: {e.nota_media(notas):.2f}")
    e.set_edad(22)
    print(f"Nueva edad: {e.get_edad()}")
