import random

# 1 - Crie um número aleatório de 5 a 10
def numero_aleatorio_5_10():
    num = random.randint(5, 10)
    return num


# 2 - Crie 3 números aleatórios
def tres_numeros_aleatorios():
    lista = []
    for i in range(3):
        lista.append(random.randint(1, 100))
    return lista


# 3 - Número aleatório entre 10 a 30 usando range
def numero_range_10_30():
    lista = list(range(10, 31))
    num = random.choice(lista)
    return num


# 4 - Contagem regressiva
def contagem_regressiva():
    for i in range(10, 0, -1):
        print(i)
    print("Fogo!")


# 5 - Soma de números pares
def soma_pares(numero):
    soma = 0

    if numero > 0:
        for i in range(2, numero + 1):
            if i % 2 == 0:
                soma += i

    return soma


# 6 - Tabuada
def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


# 7 - Números ímpares reversos
def impares_reversos():
    for i in range(99, 0, -1):
        if i % 2 != 0:
            print(i)