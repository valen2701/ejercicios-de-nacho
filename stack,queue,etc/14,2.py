nombres = ["diddy","jeffrey","azielGCM","tole","admin"]

for nombre in nombres:
    if nombre == "admin":
        print("Hola admin, ¿querés ver un informe de estado?")
    else:
        print(f"hola denuevo {nombre}")

if nombres == []:
    print("la lista esta vacia")