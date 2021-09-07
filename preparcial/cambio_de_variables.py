

if __name__ == '__main__':
    a = int(input('a:'))
    b = int(input('b:'))
    b,a = a,b
    print(f'a:{a}, b:{b}')
    b = a + b
    a = b - a
    b = b - a
    print(f'a:{a}, b:{b}')
