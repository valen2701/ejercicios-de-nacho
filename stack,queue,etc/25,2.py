def construir_perfil(nombre, apellido, **info_usuario):
    perfil = {}
    perfil['nombre'] = nombre
    perfil['apellido'] = apellido

    for clave, valor in info_usuario.items():
        perfil[clave] = valor

    return perfil


mi_perfil = construir_perfil(
    "Juan",
    "Pérez",
    edad=16,
    ciudad="Buenos Aires",
    hobby="fútbol"
)

print(mi_perfil)
