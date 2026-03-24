class Usuario:
    def __init__(self, nombre, apellido, edad, email, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.ciudad = ciudad

    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Email: {self.email}")
        print(f"Ciudad: {self.ciudad}\n")

    def saludar_usuario(self):
        print(f"Hola {self.nombre}, bienvenido!\n")


usuario1 = Usuario("Juan", "Perez", 20, "juan@gmail.com", "Buenos Aires")
usuario2 = Usuario("Maria", "Gomez", 25, "maria@gmail.com", "Cordoba")
usuario3 = Usuario("Lucas", "Fernandez", 18, "lucas@gmail.com", "Rosario")

usuario1.describir_usuario()
usuario1.saludar_usuario()

usuario2.describir_usuario()
usuario2.saludar_usuario()

usuario3.describir_usuario()
usuario3.saludar_usuario()
