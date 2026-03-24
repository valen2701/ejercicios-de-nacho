class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre_restaurante}")
        print(f"Tipo de cocina: {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"{self.nombre_restaurante} está abierto")


class PuestoDeHelados(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina, sabores):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = sabores

    def mostrar_sabores(self):
        print("Sabores disponibles:")
        for sabor in self.sabores:
            print(sabor)


puesto = PuestoDeHelados(
    "Heladería Dulce Frío",
    "Helados",
    ["Chocolate", "Vainilla", "Frutilla", "Dulce de leche"]
)

puesto.mostrar_sabores()
