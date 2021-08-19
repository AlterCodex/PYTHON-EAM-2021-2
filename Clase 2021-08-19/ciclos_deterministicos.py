"""
usted va a hacer el promedio de N numeros donde el N lo debe solicitar al
usuario al final entregara el promedio de los numeros


"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input("cantidad de numeros :"))
    prom = 0
    for i in range(0, n, 1):

        prom += int(input(f'Ingrese el numero {i}'))
    prom /= n
    print(prom)




