from functools import reduce

# Função que retorna o maior número primo em uma lista
maior_primo = lambda numeros: max(
    filter(lambda x: all(x % i != 0 for i in range(2, x)), numeros)
)

# Função que soma todos os números pares em uma lista
soma_pares = lambda numeros: reduce(
    lambda x, y: x + y, filter(lambda x: x % 2 == 0, numeros)
)

# Função que retorna uma lista com os quadrados de todos os números impares em uma lista
quadrado_impares = lambda numeros: list(
    map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numeros))
)

# Teste das funções
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(maior_primo(numeros))  # imprime 7
print(soma_pares(numeros))  # imprime 20
print(quadrado_impares(numeros))  # imprime [1, 9, 25, 81]