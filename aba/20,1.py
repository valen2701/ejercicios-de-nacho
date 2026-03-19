pedidos = ["mila", "aceituna", "queso y jamon"]
terminados = []

while pedidos:
    pedido = pedidos.pop()
    print(f"Preparé tu sándwich de {pedido}")
    terminados.append(pedido)

print(terminados)