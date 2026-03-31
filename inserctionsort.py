def inserction_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i-1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave
    return lista

print(inserction_sort([3,5,2,6,9]))