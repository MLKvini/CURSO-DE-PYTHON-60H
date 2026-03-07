import funcoes

# 1 Crie um número aleatório de 5,10
print("Número aleatório de 5 a 10:")
print(funcoes.numero_aleatorio_5_10())

# 2 Crie 3 números aleatórios
print("\n3 números aleatórios:")
print(funcoes.tres_numeros_aleatorios())

# 3  Crie um número aleatório entre 10 a 30 utilize o range()
print("\nNúmero aleatório entre 10 e 30:")
print(funcoes.numero_range_10_30())

# 4 Contagem regressiva simples
print("\nContagem regressiva:")
funcoes.contagem_regressiva()

# 5 Soma de números pares
num = int(input("\nDigite um número inteiro positivo: "))
print("Soma dos números pares:", funcoes.soma_pares(num))

# 6  Tabuada de multiplicação
num = int(input("\nDigite um número para ver a tabuada: "))
funcoes.tabuada(num)

# 7 Números ímpares reversos
print("\nÍmpares de 99 a 1:")
funcoes.impares_reversos()