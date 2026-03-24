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


class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for privilegio in self.privilegios:
            print(privilegio)


class Administrador(Usuario):
    def __init__(self, nombre, apellido, edad, email, ciudad, privilegios):
        super().__init__(nombre, apellido, edad, email, ciudad)
        self.privilegios = Privilegios(privilegios)


admin = Administrador(
    "Carlos",
    "Lopez",
    30,
    "carlos@gmail.com",
    "Buenos Aires",
    [
        "puede agregar publicaciones",
        "puede eliminar publicaciones",
        "puede bloquear usuarios"
    ]
)

admin.privilegios.mostrar_privilegios()
