
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    lista_esq = lista[:meio]
    lista_dir = lista[meio:]
    
    lista_esq = merge_sort(lista_esq)
    lista_dir = merge_sort(lista_dir)
    
    return merge(lista_esq, lista_dir)

def merge(lista_esq, lista_dir):
    lista_final = []
    i_esq, i_dir = 0, 0
    
    while i_esq < len(lista_esq) and i_dir < len(lista_dir):
        if lista_esq[i_esq] < lista_dir[i_dir]:
            lista_final.append(lista_esq[i_esq])
            i_esq += 1
        else:
            lista_final.append(lista_dir[i_dir])
            i_dir += 1
            
    lista_final += lista_esq[i_esq:]
    lista_final += lista_dir[i_dir:]
    
    return lista_final


teste = [4,5,1,2,6,7,2,3,43,21,54,67,23,12,21,23,43,44]
print(merge_sort(teste))