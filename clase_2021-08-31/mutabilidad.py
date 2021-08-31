

def agregar_a_lista(lista, valor):
    lista.append(valor)

if __name__ == '__main__':
    y = [100]
    print('antes ' + str(y))
    agregar_a_lista(y, 104)
    print(f'despues {y}')
