import random

elementos = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 'A', 'B', 'C', 'D', 'E']

ganadores = random.sample(elementos, 4)

print(f"Los números/letras ganadores son: {ganadores}")
print("Cualquier boleto que tenga estos 4 elementos gana un premio")
