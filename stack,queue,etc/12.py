# Lista original
pizzas = ["muzzarella", "pepperoni", "napolitana"]

# Copia de la lista
pizzas_amigo = pizzas[:]

# Agregar nuevas pizzas
pizzas.append("fugazzeta")
pizzas_amigo.append("calabresa")

# Mostrar listas
print("Mis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza)

print("\nLas pizzas favoritas de mi amigo/a son:")
for pizza in pizzas_amigo:
    print(pizza)