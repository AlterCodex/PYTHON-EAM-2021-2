
"""
Vamos a hacer un programa que ingrese un dato y determine si
este valor es mayor menor o igual a cero y lo imprimimos en la consola.
"""



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = int(input("--:"))
    output = 'cero'
    if number > 0:
        output = 'Mayor que Cero'
    elif number < 0:
        output = 'Menor que Cero'
    else:
        output = 'Cero'
    print(output)