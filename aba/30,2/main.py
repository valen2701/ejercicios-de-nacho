from usuarios import Administrador

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
