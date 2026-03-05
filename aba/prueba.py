lista_de_personas = ["messi", "mirtha", "azi","kristina"]
import random
import time
def send_message():
    for persona in lista_de_personas:
        print(f"Hola {persona} queres venir a comer unos asaditos a mi casa?")
        time.sleep(1)
    no_puede = random.choice(lista_de_personas)
    print(f"{no_puede} no va a poder venir")
    time.sleep(1)
    lista_de_personas.remove(no_puede)
    print(lista_de_personas)

def new_people():
    time.sleep(2)
    print("conseguimos un lugar mas grande para comer")
    time.sleep(1)
    lista_de_personas.insert(0,"aba")
    lista_de_personas.insert(2,"felix")
    lista_de_personas.insert(-1,"obama")
    print(lista_de_personas)

def cancel_party():
    for i in range(3):
        cancelar = random.choice(lista_de_personas)
        print(f"perdon {cancelar} al final no te puedo invitar")
        time.sleep(1)
        lista_de_personas.remove(cancelar)
    print(lista_de_personas)

def main():
    send_message()
    new_people()
    cancel_party()

main()