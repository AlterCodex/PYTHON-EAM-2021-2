"""
Usted va a recibir 3 numeros imprimalos de menor a mayor
AND
"""



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num1 = int(input("num1:"))
    num2 = int(input("num2:"))
    num3 = int(input("num3:"))

    if num1 <= num2 and num1 <= num3:
        print(num1)
        if num2 <= num3:
            print(num2)
            print(num3)
        else:
            print(num3)
            print(num2)
    elif num2 <= num3:
        print(num2)
        if num1 <= num3:
            print(num1)
            print(num3)
        else:
            print(num3)
            print(num1)

    else:
        print(num3)
        if num1 <= num2:
            print(num1)
            print(num2)
        else:
            print(num2)
            print(num1)



    pass