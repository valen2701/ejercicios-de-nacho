rios = {
    "nilo": "egipto",
    "amazonas": "brasil",
    "de la plata": "argentina"
}

for rio, pais in rios.items():
    print(f"El {rio.capitalize()} pasa por {pais.capitalize()}.")

for rio in rios.keys():
    print(rio.capitalize())

for pais in rios.values():
    print(pais.capitalize())