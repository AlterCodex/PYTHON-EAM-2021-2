"""
usted se va a encargar de determinar si una empresa esta en riesgo.
para ello se van a ingresar 3 valores numericos que representan las
calificaciones promedio que han dado las calificadoras de riesgo.

"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num1 = int(input("num1:"))
    num2 = int(input("num2:"))
    num3 = int(input("num3:"))
    #si 3 de 3 calificaciones son mayores a 6 se imprimira "Confiable"
    if num1 > 6 and num2 > 6 and num3 > 6:
        print("Confiable")
    #si Almenos 1 Calificacion es 0 se debe imprimir "Advertencia"
    elif num1 == 0 or num2 == 0 or num3 == 0:
        print("Advertencia")
    #si 2 de 3 calificaciones son mayores 5 se imprimira "Semi Confiable: " y el
    #promedio de la calificacion.
    elif (num1 > 5 and num2 > 5) or (num2 > 5 and num3 > 5)\
            or (num1 > 5 and num3 > 5):
        print("Semi Confiable")
        promedio = (num1+num2+num3)/3
        print(promedio)
