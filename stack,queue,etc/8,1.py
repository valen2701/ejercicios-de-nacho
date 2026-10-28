def check_string(str):
    #isprintable() sirve para verificar que un string se puede mostrar en pantalla con todos sus caracteres
    #no toma algunos como \n \t \m
    if str.isprintable() == True:
        #isspace() verifica que no haya espacio en el string
        if str.isspace() == False:
            print("la palabra es correcta")
        else:
            print("la palabra tiene espacios")
    else:
        print("no es printeable")
    main()

def main():
    str = input("Ingrese una palabra: ")
    check_string(str)
main()