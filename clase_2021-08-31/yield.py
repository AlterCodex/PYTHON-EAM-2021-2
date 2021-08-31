#http://images.math.cnrs.fr/El-problema-3n-1-elemental-pero-temible-I.html
# ?lang=fr
# HIPOTESIS " TODO NUMERO QUE SE TRANFORME BAJO LAS REGLAS CONVERGE EN 1
# REGLAS: SI N ES 1 TERMINE
#         SI N ES PAR  N // 2
#         SI N no ES PAR 3*N+1




def TreeNplus1(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n+1
    yield n


if __name__ == '__main__':
    for i in TreeNplus1(5):
        print(i)