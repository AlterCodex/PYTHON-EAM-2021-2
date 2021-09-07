

if __name__ == '__main__':
    n = int(input("Ingrese el numero a validar:"))
    suma = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            suma += i
    if suma == n:
        print("perfecto")
    else:
        print("imperfecto")