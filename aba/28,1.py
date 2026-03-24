class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = 0

    def describir_restaurante(self):
        print(f"Restaurante: {self.nombre_restaurante}")
        print(f"Tipo de cocina: {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"{self.nombre_restaurante} está abierto")

    def establecer_clientes_atendidos(self, cantidad):
        self.clientes_atendidos = cantidad

    def incrementar_clientes_atendidos(self, cantidad):
        self.clientes_atendidos += cantidad


restaurante = Restaurante("La Buena Pasta", "Italiana")

print(restaurante.clientes_atendidos)

restaurante.clientes_atendidos = 50
print(restaurante.clientes_atendidos)

restaurante.establecer_clientes_atendidos(120)
print(restaurante.clientes_atendidos)

restaurante.incrementar_clientes_atendidos(30)
print(restaurante.clientes_atendidos)

