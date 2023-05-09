
def quickSort (lista,inicio = 0,fim = None):
    if len(lista) <= 1:
        return lista

    if fim is None:
        fim = len(lista) - 1
    
    if inicio < fim:
        p = partition(lista,inicio,fim)
        quickSort(lista,inicio,p - 1)
        quickSort(lista,p + 1, fim)
    
    return lista

def partition(lista,inicio,fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio,fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    
    return i

# def quickSort(lista):
#     if len(lista) <= 1:
#         return lista
    
#     pivot = lista[0]
#     menores = [elem for elem in lista[1:] if elem < pivot]
#     maiores = [elem for elem in lista[1:] if elem >= pivot]
    
#     return quickSort(menores) + [pivot] + quickSort(maiores)


# def quickSort(lista):
#     if len(lista) <= 1:
#         return lista
    
#     pivot = lista[0]
#     menores, maiores = particionar(lista[1:], pivot)
    
#     return quickSort(menores) + [pivot] + quickSort(maiores)

# def particionar(lista, pivot):
#     menores = []
#     maiores = []
    
#     for elem in lista:
#         if elem < pivot:
#             menores.append(elem)
#         else:
#             maiores.append(elem)
    
#     return menores, maiores





teste = [4,5,1,2,6,7,2,3,43,21,54,67,23,12,21,23,43,44]
print(quickSort(teste))
    