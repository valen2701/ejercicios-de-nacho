from usuario import Usuario

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
