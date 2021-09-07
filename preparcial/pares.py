if __name__ == '__main__':
    n = int(input("n:"))
    pares = True
    for i in range(n):
        k = int(input(f"deme el valor {i+1} :"))
        pares = pares and k % 2 == 0
    if pares:
        print("Todos son PARES")
    else:
        print("No todos son pares")
