print('***** Exercício 06 *****')

# Deseja-se completar um programa que gera números pseudoaleatórios
# entre 20 e 99 e os mostre escritos por extenso.
# Para isso, você deve completar as funções
# - dezena_por_extenso: recebe um número de 2 a 9 e retorna "vinte" a "noventa"
# - unidade_por_extenso: recebe um número de 0 e 9 e retorna a unidade por extenso
# O restante do programa deve ficar inalterado
# Ao final do programa, há 2 exemplos com lógica semelhante que podem servir
# de referência

# Exemplo de saída do programa
# sessenta e quatro
# oitenta e três
# vinte e um
# noventa
# vinte e oito
# sessenta e nove
# setenta e seis
# setenta e oito
# setenta e quatro
# trinta e oito
    
def dezena_por_extenso(n):
  if n == 2: return 'vinte'
  elif n == 3: return 'trinta'
  elif n == 4: return 'quarenta'
  elif n == 5: return 'cinquenta'
  elif n == 6: return 'sessenta'
  elif n == 7: return 'setenta'
  elif n == 8: return 'oitenta'
  elif n == 9: return 'noventa'
def unidade_por_extenso(n):
  if   n == 1: return 'um'
  elif n == 2: return 'dois'
  elif n == 3: return 'três'
  elif n == 4: return 'quatro'
  elif n == 5: return 'cinco'
  elif n == 6: return 'seis'
  elif n == 7: return 'sete'
  elif n == 8: return 'oito'
  elif n == 9: return 'nove'
    
def por_extenso(n):
  if n < 20 or n > 99:
    return "Número inválido"
  else:
    dezena = n // 10
    unidade = n % 10
    if unidade > 0:
      return dezena_por_extenso(dezena) + ' e ' + unidade_por_extenso(unidade)
    return dezena_por_extenso(dezena)

from random import randint
i = 0
while i < 10:
  n = randint(20,99)
  print(por_extenso(n))
  i += 1

# Exemplos de funções com lógica semelhante.
# A primeira versão usa só condicionais
# A segunda versão usa uma lista
# def dia_da_semana_v1(n):
#   if   n == 1: return 'Dom'
#   elif n == 2: return 'Seg'
#   elif n == 3: return 'Ter'
#   elif n == 4: return 'Qua'
#   elif n == 5: return 'Qui'
#   elif n == 6: return 'Sex'
#   elif n == 7: return 'Sab'
#   else: return ''

# def dia_da_semana_v2(n):
#   dias = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
#   if n < 1 or n > 7:
#     return ''
#   else:
#     return dias[n-1]

print('***** Exercício 02 *****')
print("Em uma pizzaria chamada Unilanches Catuípe é oferecido um desconto por via dos sabores que o cliente procura ")
print('Neison, Diego e Artur, estavam com muita fome devido a isso, resolveram ir na Unilanches Catuípe depois de "Ignaitar um Maokai 100% legalizado".')
print('Na pizzaria escolheram os seguintes sabores')

from random import choice
pizzas = []
while len(pizzas) <= 7:
  pizza = choice(['Calabresa','Filé alho e óleo', 'Filé Mostarda','Lombinho Canadense','Basca','Coração','4 queijos'])
  pizzas.append(pizza)
print(pizzas)
print(len(pizzas),'foram escolhidas, das quais foram', pizzas.count('Filé Mostarda'),'Filé Mostarda que Artur adora, Oba!')
print('A ordem delas foi, feita assim')
i = 0
while i < len(pizzas):
  pizza_selecionada = pizzas[i]
  if pizza_selecionada == 'Filé Mostarda':
    i+= 1
    print('Pizza {}: {}'.format(i,pizza_selecionada))
    print('Oba!')
  else:
    i+= 1
    print('Pizza {}: {}'.format(i,pizza_selecionada))
# Uma pizzaria oferece desconto
# para o "sabor do dia", que é
# definido por sorteio a partir
# de uma lista de sabores.

# Escreva um programa que sorteie
# um sabor 7 vezes (um para cada
# dia da semana) e, caso o sabor
# seja o seu preferido, mostre na
# tela "Oba!"

# Observações:
# - Você deve escolher um preferido, mesmo que não goste de pizza :-)
# - Você deve usar while
# - Lembre da função choice, que sorteia um elemento de uma lista

# Exemplo de saída:

# Dia 1 : Bacon
# Dia 2 : Calabresa
# Dia 3 : Marguerita
# Oba!
# Dia 4 : Calabresa
# Dia 5 : Bacon
# Dia 6 : Marguerita
# Oba!
# Dia 7 : Calabresa

print('***** Exercício 03 *****')
print('David foi um grande joia da base Corinthians em meados 2010, em sua carreira ele foi para a Europa aos 14 anos no ano de 2015, com um físico invejavel, mente blindada e coach de Paulo Guina e Erico Rocha, apenas....')
print('Ele foi goleador nos anos:')
from random import randint

x = 0
y = []
while x <= 4:
  ano = randint(2010,2020)
  print(ano)
  if ano > 2015:
    y.append(ano)
  x += 1
else:
  print(ano)

print('David foi goleador na europa {} vezes'.format(len(y)))
# Escreva um programa que gere e mostre 5 
# números pseudoaleatórios representando 
# anos no período entre 2010 e 2020 (inclusive).
# No final, o programa deve mostrar quantos
# números gerados são maiores que 2015

# Exemplo de saída:
# 2020
# 2012
# 2015
# 2020
# 2016
# Maiores que 2015: 3


  print('***** Exercício 04 *****')
from math import sqrt
# (Adaptado de: https://programming-23.mooc.fi/part-2)
# Escreva um programa que use a função input repetidamente
# para entrada (leitura) de um número inteiro.
# Se o número for negativo, o programa deve mostrar a
# mensagem "Número inválido"
# Se o número for maior do que zero, o programa deve
# mostrar a raiz quadrada do número
# Em qualquer desses casos, o programa deve continuar
# solicitando a digitação do próximo número
# Se o número for igual a zero, o programa deve mostrar
# uma mensagem e sair do laço
# Dica: converta para inteiro a string lida
# pela função input
print('Descubra a raiz quadrada de qualquer número, mas não coloque uma raiz invalida!!')
while True:
  x = int(input("Insira um Número"))
  if x < 0:
    print('Número inválido')
    break
  else:
    print(sqrt(x))
    
    
# Exemplo de execução
# Digite um número: 9
# 3.0
# Digite um número: 4
# 2.0
# Digite um número: 6
# 2.449489742783178
# Digite um número: -2
# Número inválido
# Digite um número: 0
# Terminando...

print('***** Exercício 05 *****')

# Fonte: https://programming-23.mooc.fi/part-2
# Deseja-se mostrar uma contagem regressiva
# como no exemplo abaixo:

# Countdown!
# 5
# 4
# 3
# 2
# 1
# Now!

# O código abaixo tenta fazer isso, mas tem
# um erro. Corrija-o para obter a saída desejada.
number = 5
print("Countdown!")
while True:
  print(number)
  number -= 1
  if number == 0:
    print(number)
    break
print("Now!")
print('***** Exercício 08 *****')
print('A casa de Gabriel')
from random import randint
# Um sistema de automação residencial possui sensores de temperatura
# que, periodicamente, produzem uma lista de valores representando
# um conjunto de temperaturas medidas.
# De vez em quando, alguns sensores falham e retornam medidas absurdas,
# incompatíveis com a localidade e a estação do ano.
# Sua tarefa é criar uma função que receba uma lista e 2 números
# representando limiares de temperatura, e verifique se todos os elementos
# da lista estão dentro dos limiares. A função deverá retornar True se todos
# os elementos estiverem dentro dos limiares, ou False em caso contrário.

# Dica: um laço while pode ser interrompido com return

# Exemplo de uso:
# temperaturas = [32,31,22,33,34]
# temperaturas_validas(temperaturas, 0, 40)
# True
# temperaturas = [32,31,22,-99,33,34]
# temperaturas_validas(temperaturas, 0, 40)
# False
lista = []
def temperaturas_validas(lista, inferior, superior):
  i = 0
  while i < len(lista):
    temperatura_selecionada = lista[i]
    if (temperatura_selecionada < inferior or temperatura_selecionada > superior):
        return False
    
    i += 1
    if(i == len(lista)):
        return True

temperaturas = [32,31,22,33,34]
print(temperaturas_validas(temperaturas, 0, 40)) # deve retornar True
temperaturas = [32,31,22,-99,33,34]
print(temperaturas_validas(temperaturas, 0, 40)) # deve retornar False

print('***** Exercício 09 *****')

# O CPF é um número de 11 dígitos, sendo que
# os 2 últimos são dígitos verificadores, calculados a partir
# dos anteriores
# Dada uma lista de números representando um CPF, sua tarefa será
# elaborar uma função que valide o primeiro dígito verificador.

# O cálculo segue o seguinte procedimento:

# Tome como exemplo este CPF: 
# 556.678.840-89

# 1) Calcula-se o somatório dos 9 primeiros dígitos multiplicados por 10, 9, ...
#  5  5  6  6  7  8  8  4  0 
#  x  x  x  x  x  x  x  x  x  
# 10  9  8  7  6  5  4  3  2
# = 5*10 + 5*9 + 6*8 + 6*7 + 7*6 + 8*5 + 8*4 + 4*3 + 0*2
# = 311

# 2) Calcula-se o resto da divisão do somatório por 11
# 311 % 11 = 3

# 3) Se resto < 2, o dígito é 0. Caso contrário, o dígito é 11-resto
# 11 - 3 = 8
def valida_digito1(cpf):
    if len(cpf) != 11:
        return False
    
    soma = 0
    for i in range(9):
        soma += cpf[i] * (10 - i)
    
    resto = soma % 11
    if resto < 2:
        valida_digito1 = 0
    else:
        valida_digito1 = 11 - resto
    
    return cpf[9] == valida_digito1 
  
        
