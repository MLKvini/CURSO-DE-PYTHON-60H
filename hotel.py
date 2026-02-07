print('HOTEL')
print('-'*30)

print("=== Cadastro de Clientes ===")
cliente1_nome = input("Digite o nome do cliente 1: ")
cliente1_idade = int(input("Digite a idade do cliente 1: "))

cliente2_nome = input("Digite o nome do cliente 2: ")
cliente2_idade = int(input("Digite a idade do cliente 2: "))

cliente3_nome = input("Digite o nome do cliente 3: ")
cliente3_idade = int(input("Digite a idade do cliente 3: "))
print('-'*30)

preco_simples = 100
preco_duplo = 150
preco_luxo = 250

print("\n=== Reserva de Quartos ===")
print("Opções de quartos: Simples, Duplo, Luxo")

cliente1_quarto = input(f"Escolha o quarto do {cliente1_nome}: ")
cliente2_quarto = input(f"Escolha o quarto do {cliente2_nome}: ")
cliente3_quarto = input(f"Escolha o quarto do {cliente3_nome}: ")

cliente1_dias = int(input(f"Quantos dias {cliente1_nome} ficará no hotel? "))
cliente2_dias = int(input(f"Quantos dias {cliente2_nome} ficará no hotel? "))
cliente3_dias = int(input(f"Quantos dias {cliente3_nome} ficará no hotel? "))

if cliente1_quarto.lower() == "simples":
    valor_cliente1 = preco_simples * cliente1_dias
elif cliente1_quarto.lower() == "duplo":
    valor_cliente1 = preco_duplo * cliente1_dias
elif cliente1_quarto.lower() == "luxo":
    valor_cliente1 = preco_luxo * cliente1_dias
else:
    valor_cliente1 = 0
    print(f"Quarto nao disponivel para {cliente1_nome}!")

if cliente2_quarto.lower() == "simples":
    valor_cliente2 = preco_simples * cliente2_dias
elif cliente2_quarto.lower() == "duplo":
    valor_cliente2 = preco_duplo * cliente2_dias
elif cliente2_quarto.lower() == "luxo":
    valor_cliente2 = preco_luxo * cliente2_dias
else:
    valor_cliente2 = 0
    print(f"Quarto inválido para {cliente2_nome}!")

if cliente3_quarto.lower() == "simples":
    valor_cliente3 = preco_simples * cliente3_dias
elif cliente3_quarto.lower() == "duplo":
    valor_cliente3 = preco_duplo * cliente3_dias
elif cliente3_quarto.lower() == "luxo":
    valor_cliente3 = preco_luxo * cliente3_dias
else:
    valor_cliente3 = 0
    print(f"Quarto inválido para {cliente3_nome}!")

print("\n=== Valores das Estadas ===")
print(f"{cliente1_nome} deve pagar: R$ {valor_cliente1:.2f}")
print(f"{cliente2_nome} deve pagar: R$ {valor_cliente2:.2f}")
print(f"{cliente3_nome} deve pagar: R$ {valor_cliente3:.2f}")

formas_pagamentos =  ['pix','cc','cd']
print('escolha a  forma de pagamento: ', formas_pagamentos)
escolhe_forma = input('Digite a forma de pagamento: ')
indice = formas_pagamentos.index(escolhe_forma)
print('Forma de pagamento: ', formas_pagamentos[indice])
print('volte sempre! ')
