# Seleciona o MENOR elemento e vai encaixando ele dentro do Array

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        idx_min = i
        for j in range(i+1, n):
            if lista[j] < lista[idx_min]:
                lista[j], lista[idx_min] = lista[idx_min], lista[j]
    return lista
print(selection_sort([1,2,50,20,44]))
