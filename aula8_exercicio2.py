#EXERCÍCIOS 1: 
#Utilize condicionais

#Acessar a Aula - 8

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
num = int(input('coloca algum numero:'))
if num >= 1:
    print('numero positivo')
else:
    print('numero negativo')
if num == 0:
        print('esse é o numero zero')
else:
        print('esse nao é o zero')
# 2*
# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
num1 = int(input('coloca a sua idade: '))
if num1 >= 18:
      print('pode votar')
else:
      print("nao pode votar")
# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.
num2 = int(input('coloca um numero: '))
if num2 % 2 == 0:
      print(f'o numero {num2} é par')
else:
      print(f'o numero {num2} é impar')
# 4*
# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
num3 = float(input("Primeiro lado: "))
num4 = float(input("Segundo lado: "))
num5 = float(input("Terceiro lado: "))

# Verifica se pode formar triângulo
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

if num3 + num4 > num5 and num3 + num5 > num4 and num4 + num5 > num3:
    if num3 == num4 == num5:
        print("Equilátero")
    elif num3 == num4 or num3 == num5 or num4 == num5:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não forma triângulo")

# 5*

	# Determine se um número é múltiplo de 5 e 7.
     
num6 = int(input("Digite um número: "))
if num6 % 5 == 0 and num6 % 7 == 0:
    print("É múltiplo de 5 e 7")
else:
    print("Não é múltiplo de 5 e 7")
# 6*
# Verifique se um número é positivo e maior que 10
num7 =  int(input('coloca um numero que é maior que 10'))
if num7 > 0 and num7 > 10:
     print('o numero é maior que 10 e positivo')
else:
     print('o numero nao é maior que 10 e nao é positivo')

# 7*
# Verifique se um número é divisível por 3 ou 5.

num8 = int(input("Digite um número: "))
if num8 % 3 == 0 or num8 % 5 == 0:
    print("O numero é divisivel por 3 ou 5")
else:
    print("O numero nao é divisível por 3 nem por 5")