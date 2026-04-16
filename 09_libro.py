GENEROS_FICCION = {
    "ficción", "ciencia ficción", "fantasía", "novela", "cuento",
    "thriller", "misterio", "romance", "horror", "aventura"
}

class Libro:
    def __init__(self, titulo: str, autor: str, genero: str, paginas: int):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._paginas = paginas

    # --- Getters ---
    def get_titulo(self): return self._titulo
    def get_autor(self): return self._autor
    def get_genero(self): return self._genero
    def get_paginas(self): return self._paginas

    # --- Setters ---
    def set_titulo(self, titulo: str): self._titulo = titulo
    def set_autor(self, autor: str): self._autor = autor
    def set_genero(self, genero: str): self._genero = genero
    def set_paginas(self, paginas: int):
        if paginas <= 0:
            raise ValueError("El número de páginas debe ser positivo.")
        self._paginas = paginas

    def es_ficcion(self) -> bool:
        return self._genero.lower() in GENEROS_FICCION

    def __str__(self):
        tipo = "Ficción" if self.es_ficcion() else "No ficción"
        return (
            f"'{self._titulo}' de {self._autor} | Género: {self._genero} | "
            f"Páginas: {self._paginas} | Tipo: {tipo}"
        )


# --- Ejemplo de uso ---
if __name__ == "__main__":
    libro1 = Libro("Dune", "Frank Herbert", "Ciencia ficción", 412)
    libro2 = Libro("Sapiens", "Yuval Noah Harari", "Historia", 443)
    print(libro1)
    print(libro2)
    print(f"¿'{libro1.get_titulo()}' es ficción? {libro1.es_ficcion()}")
    print(f"¿'{libro2.get_titulo()}' es ficción? {libro2.es_ficcion()}")
