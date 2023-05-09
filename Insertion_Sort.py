
def insertionSort(lista:list) -> list:
    if len(lista) <= 1:
        return lista
    
    for i in range(1,len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave
    
    return lista

teste = [3,4,1,2,6,7,4,9,0]
print(insertionSort(teste))

    
