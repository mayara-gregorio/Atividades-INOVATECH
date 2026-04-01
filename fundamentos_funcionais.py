#def saudacao(nome):
#    return f'Olá, {nome}'

###função passada em uma variável
#cumprimentar = saudacao
#print(cumprimentar('Mayara'))

##função passada como argumento
#def execultar(funcao, nomePessoa):
#    return funcao(nomePessoa)
#print(execultar(saudacao, 'Mayara'))

#################################

##função lambda, função anônima
#numero = lambda x: x + 5 #mesmo que def somar(x): return x + 5
#print(numero(5))

#nomes = ['Zelia', 'Paulo', 'Auriany']
#nomes.sort(key=lambda n: len(n), reverse=True)
#print(nomes)

##map
numeros = [1,3,5,6,7,8,9,2]

#quadrados = [list(map(lambda x: x**2, numeros))]
#quadrados = [x**2 for x in numeros]

#pares = list(filter(lambda x:x%2==0, numeros))
#pares = [x for x in numeros if x%2 == 0]

from functools import reduce

soma = reduce(lambda acum, x: acum + x, filter(lambda x: x < 4, numeros),0)
print(soma)