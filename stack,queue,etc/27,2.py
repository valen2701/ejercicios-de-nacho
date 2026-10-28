class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre_restaurante}")
        print(f"Tipo de cocina: {self.tipo_cocina}\n")

    def abrir_restaurante(self):
        print(f"{self.nombre_restaurante} está abierto 🍽️")

restaurante1 = Restaurante("La Buena Pasta", "Italiana")
restaurante2 = Restaurante("El Asador", "Parrilla")
restaurante3 = Restaurante("Sushi World", "Japonesa")


restaurante1.describir_restaurante()
restaurante2.describir_restaurante()
restaurante3.describir_restaurante()
