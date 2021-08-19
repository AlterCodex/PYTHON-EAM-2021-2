"""
Vamos a hacer un programa que ingrese un dato y determine si
este valor es mayor menor o igual a cero y lo imprimimos en la consola.
hasta que el usuario ingrese un 0.
"""



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = 8
    while number != 0:
        number = int(input("--:"))
        if number > 0:
            print('Mayor que cero')
        elif number < 0:
            print('Menor que cero')
        else:
            print('Cero')



