

if __name__ == '__main__':
    n = 800
    total = 0
    while n > 0:
        n = int(input("indique el valor de las toneladas:"))
        descuento = 1
        if 0 < n < 10:
            descuento=0
        elif 10 <= n < 20:
            descuento = 0.05
        elif 20 <= n < 30:
            descuento = 0.15
        elif 30 <= n:
            descuento = 0.3
        precio_bruto = abs(n) * 1000
        precio_neto = precio_bruto - (precio_bruto*descuento)
        total += precio_neto
    print(total)