usuarios_actuales = ["diddy","jeffrey","azielGCM","tole","totote"]

usuarios_nuevos = ["totote","chaparrin","sabion","azielGCM","DIGJ0AOOO"]

usuarios_actuales_minusculas = []
for usuario in usuarios_actuales:
    usuarios_actuales_minusculas.append(usuario.lower())


for usuario in usuarios_nuevos:
    if usuario.lower() in usuarios_actuales_minusculas:
        print(f"El nombre de usuario '{usuario}' ya está en uso. Elegí otro.")
    else:
        print(f"El nombre de usuario '{usuario}' está disponible.")