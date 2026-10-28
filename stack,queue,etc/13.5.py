
frutas_favoritas = ["frutilla", "ciruela", "manzana", "pera"]

print("Decime tus 3 frutas favoritas:")
fruta1 = input("Fruta 1: ")
fruta2 = input("Fruta 2: ")
fruta3 = input("Fruta 3: ")


fruta_usuario = [fruta1, fruta2, fruta3]

for fruta in fruta_usuario:
    if fruta in frutas_favoritas:
        print(f"Te gusta la {fruta} como a mi")