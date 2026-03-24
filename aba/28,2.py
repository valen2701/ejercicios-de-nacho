class Usuario:
    def __init__(self, nombre, apellido, edad, email, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.ciudad = ciudad
        self.intentos_login = 0

    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Email: {self.email}")
        print(f"Ciudad: {self.ciudad}\n")

    def saludar_usuario(self):
        print(f"Hola {self.nombre}, bienvenido!\n")

    def incrementar_intentos_login(self):
        self.intentos_login += 1

    def reiniciar_intentos_login(self):
        self.intentos_login = 0


usuario = Usuario("Juan", "Perez", 20, "juan@gmail.com", "Buenos Aires")

usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()
usuario.incrementar_intentos_login()

print(usuario.intentos_login)

usuario.reiniciar_intentos_login()

print(usuario.intentos_login)
