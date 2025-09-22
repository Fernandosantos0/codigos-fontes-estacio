# 2. Iterando sobre string
for letra in 'Python':
    print(letra)

# 3. Iterando sobre lista
frutas = ['maçã', 'banana', 'uva']
for fruta in frutas:
    print(fruta)

# 4. Iterando sobre tupla
cores = ('vermelho', 'verde', 'azul')
for cor in cores:
    print(cor)

# 5. Iterando sobre dicionário
aluno = {'nome': 'Rafael', 'idade': 30, 'curso': 'Python'}
for chave in aluno:
    print(chave, aluno[chave])

for valor in aluno.values():
    print(valor)

for chave, valor in aluno.items():
    print(chave, valor)

# 6. Iterando sobre conjunto (set)
numeros = {1, 2, 3, 4, 5}
for n in numeros:
    print(n)

# 7. List Comprehension
quadrados = [x**2 for x in range(6)]
print(quadrados)