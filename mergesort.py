def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i+=1
        else:
            resultado.append(dir[j])
            j+=1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado

print(merge_sort([38,27,43,3]))