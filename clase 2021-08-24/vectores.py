
# implementar el algoritmo de burbuja para ordenar un vector

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vector = [8,5,4,3,8,6,7]
    for i in range(len(vector)):
        burbuja = vector[i]
        vector[i] = ''
        for j in range(i+1,len(vector)):
            print(burbuja)
            print(vector)
            if vector[j] < burbuja:
                temp = vector[j]
                vector[j] = burbuja
                burbuja = temp

        vector[i] = burbuja
    print(dir([]))