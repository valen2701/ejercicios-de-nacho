import time
lugares = ["Puerto Rico", "Madrid", "París", "Londres", "Nueva York"]
def main():
    imprimir_lugares()

    
def imprimir_lugares():
    print(lugares)
    time.sleep(1)
    print(f"la lista ordenada es: {sorted(lugares)}")
    time.sleep(1)
    print(lugares)
    time.sleep(1)
    print(f"la lista ordenada al revés es: {sorted(lugares, reverse=True)}")
    time.sleep(1)
    print(lugares)
    time.sleep(1)



main()