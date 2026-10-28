def hacer_auto(fabricante, modelo, **info_extra):
    auto = {}
    auto['fabricante'] = fabricante
    auto['modelo'] = modelo

    for clave, valor in info_extra.items():
        auto[clave] = valor

    return auto


auto = hacer_auto('toyota', 'corolla', color='gris', airbags=True)


print(auto)
