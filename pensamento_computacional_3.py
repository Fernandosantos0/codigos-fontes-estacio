# Programa para calcular a média de uma lista de números

# Declaração de lista de números
numeros = [2, 4, 6, 8, 10]

# Inicialização da variável soma
soma = 0

# Cálculo do comprimento da lista
n = len(numeros)

# Laço de repetição para somar os números
for numero in numeros: 
    soma += numero
    
# Cálculo da média
media = soma / n

# Impressão do resultado
print("A média é:", media)