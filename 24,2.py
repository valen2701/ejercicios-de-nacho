mensajes = ["hola", "como va", "todo bien"]
enviados = []

def enviar_mensajes(lista, enviados):
    while lista:
        mensaje = lista.pop()
        print(mensaje)
        enviados.append(mensaje)

enviar_mensajes(mensajes, enviados)

print(mensajes)
print(enviados)