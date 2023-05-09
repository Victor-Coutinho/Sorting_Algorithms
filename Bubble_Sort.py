
def bubbleSort(lista:list) -> list:
    if len(lista) <= 1:
        return lista
    
    for j in range(len(lista) - 1):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return lista

teste = [3,4,1,2,6,7,4,9,0]
print(bubbleSort(teste))