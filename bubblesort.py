def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

listanumeros = [1, 34, 1, 33, 989, 345]
print(bubble_sort(listanumeros))