#Busca linear, para elementos ordenados ou não

def busca_linear(num, lista):
    n = len(lista)
    for i in range (n):
        if lista[i] == num:
            return i
    return -1

print(f'Índice do elemento: ', busca_linear(3, [1,5,3,8]))