
def selectionSort (lista:list) -> list:
    if len(lista) <= 1:
        return lista
    
    for j in range(len(lista) - 1):
        menor_index = j
        for i in range(j,len(lista)):
            if lista[i] < lista[menor_index]:
                menor_index = i
    
        if lista[j] > lista[menor_index]:
            aux = lista[j]
            lista[j] = lista[menor_index]
            lista[menor_index] = aux

    return lista

# def ordenSel(lista):
#   ordenada = []

#   for j in range(len(lista)):
#       menor = lista[0]
#       for i in range(len(lista)):
#           if menor > lista[i]:
#               menor = lista[i]

#       ordenada.append(menor)
#       lista.remove(menor)
  
#   lista = ordenada  
#   return lista


# def ordenSelo(lista): #ondenação por seleção sem criar um novo vetor 
#   for j in range(len(lista)):
#       menor = lista[j]
#       for i in range(j,len(lista)):
#           if menor > lista[i]:
#               menor = lista[i]
#       lista.remove(menor)
#       lista.insert(j,menor)
  
#   return lista

        
teste = [3,2,1,5,6,3,1,3]
print(selectionSort(teste))