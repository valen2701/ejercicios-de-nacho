import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


dado6 = Die()
for _ in range(10):
    dado6.roll_die()

dado10 = Die(10)
for _ in range(10):
    dado10.roll_die()

dado20 = Die(20)
for _ in range(10):
    dado20.roll_die()
