lenguajes_favoritos = {
    "Juan": "python",
    "marlon": "c++",
    "tomey": "java",
    "pepe": "c#"
}

personas = ["Juan", "pepe", "tomey", "manu", "Pedro"]

for persona in personas:
    if persona in lenguajes_favoritos:
        print(f"Gracias {persona} por responder la encuesta.")
    else:
        print(f"{persona}, te invitamos a responder la encuesta.")