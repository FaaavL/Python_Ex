print('********** Questão 1 **********')

# Escreva uma função em Python nomeada `delta` para calcular
# o discriminante de uma função quadrática, 
# dados seus coeficientes a, b, c
# Calcule o `delta` conforme estas orientações:
# https://brasilescola.uol.com.br/matematica/relacao-parabola-com-delta-funcao-segundo-grau.htm

from random import randint
a = randint(-1,10)
b = randint(-4,9)
c = randint(10,20)

def delta1(a,b,c):
  return b**2-4*a*c
print(delta1(a,b,c))

print('********** Questão 2 **********')
# Escreva um programa que:
# - gere 3 valores de coeficientes a, b, c de una função quadrática
# - calcule o delta usando a função do exercício anterior
# - mostre os valores de a, b, c
# - mostre o valor do delta
# - informe se a função terá duas, uma ou nenhuma raiz real, 
#   dependendo do valor do delta 
#   (consulte o link do exercício anterior para saber as condições)
#   Exemplo de saída:
#     a = 6 b = 5 c = 1
#     delta = 1
#     duas raízes reais

def delta(a,b,c):
    return b**2-4*a*b
  
a = randint(-1,2)
b = randint(-4,9)
c = randint(-4,9)
if delta(a,b,c) >= 0:
  print('função possui duas raízes reais diferentes')
elif delta(a,b,c) == 0:
  print('A função possui uma única raiz real')
else:  
  print('A função não possui uma raiz real')
print('delta =',delta(1,4,3))
print('a =',a)
print('b =',b)
print('c =',c)


print('********** Questão 3 **********')

# Exercício adaptado de: 
# https://programming-22.mooc.fi/part-1/5-conditional-statements
print('Em um mundo remoto, longe de qualquer reduto humano. Zaratrusta está sob imprevíveis ameaças meteorológicas, que são informadas 30 minutos antes para ele atraves de um celular da Google.')
print('Zaratrusta está verificando, e visualiza em seu celular da Google: ')
from random import randint
a = randint(0,1)
c = randint(0,40)
def dia(c,a):
  print('O celular expõe:')
  if c <= 10 and a == 0:
    return 'Zaratrusta você precisa se agassalhar fará muito frio'
  elif c <= 20 and a == 0:
    return 'Zaratrusta você está bem, haverá um clima bom, sem chuvas'
  elif c <= 30 and a == 0:
    return'Zaratrusta estará quente, tome bastante água pois o tempo estará muito seco'
  elif c <= 10 and a ==1:
    return 'Zaratrusta você precisa fazer uma fogueira, irá nevar'
  elif c <= 20 and a == 1:
    return 'Zaratrusta você está bem, haverá um clima bom com uma chuva leve'
  elif c <= 30 and a == 1:
    return'Zaratrusta estará quente e fará uma chuva refrescante '
  else:
    return 'Estamos fora do ar, =('
print(dia(c,a))
print( 'Zaratrusta pergunta-se:')
print('  -isto seria um paraiso solitário ou um pesadelo da solidão?')



print('********** Questão 4 **********')

# O IBGE oferece um serviço de consulta de frequência de nomes:
# https://servicodados.ibge.gov.br/api/docs/nomes?versao=2
# As séries de dados estão organizadas por décadas, de 1930 a 2010
# Uma das consultas possíveis é o ranking de nomes por década:
# https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?decada=2010
# Para fazer esta consulta, precisamos fornecer um ano válido,
# pois do contrário o serviço não retornará dados
# Ao todo, há 9 valores válidos, de 1930 a 2010 (inclusive)
# Somente é válido o ano de início de uma década. 
# Por exemplo, 1940 é válido, mas 1941 não é

# Sabendo disso, defina uma função `valida_ano(ano)`, que retorne
# True se o ano for válido ou False se não for
# Exemplos de uso da função:
# >>> valida_ano(1930)
# True
# >>> valida_ano(2013)
# False


# COMPLETE-ME

ano = randint(1930,2010)
def valida_ano(ano):
  if ano == 1930:
    return 'True'
  elif ano == 1940:
    return 'True'
  elif ano == 1950:
    return 'True' 
  elif ano == 1960:
    return 'True'  
  elif ano == 1970:
    return 'True'
  elif ano == 1980:
    return 'True'
  elif ano == 1990:
    return 'True'
  elif ano == 2000:
    return 'True'
  elif ano == 2010:
    return 'True'
  else:
    return 'False'
print('A data verificada é', ano)
print('A data tem dado,',valida_ano(ano))
print('********** Questão 5 **********')


# Adaptado de: https://novatec.com.br/livros/introducao-python-3ed/
# Escreva uma função nomeada `aprova_emprestimo`, que retorne
# True ou False, aprovando ou não um empréstimo bancário para 
# compra de uma casa. 
# Essa função deve receber como argumentos: 
# o valor da casa a comprar, 
# o salário do solicitante e o
# prazo de pagamento do empréstimo, em anos. 
# Para aprovação, o valor da prestação mensal não pode ser superior 
# a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar
# dividido pelo número de meses a pagar.

# Exemplo de uso da função:
# >>> aprova_emprestimo(200000, 5500, 10)
# False
# >>> aprova_emprestimo(200000,5800,10)
# True

# COMPLETE-ME

vcc = randint(1,100000)
sc = randint(1,100000)
pp = randint(1,10)

def aprova_emprestimo(vcc,pp,sc):
  return (vcc/pp)/sc

print('o salário do contratante é',sc,'reais')
print('o valor da casa é', vcc,'reais')
print('A alienação final do produto será em',pp,'anos')

print(' Portanto o crédito terá como decisão do Banco:')
  
if aprova_emprestimo(vcc,pp,sc) >= 0.3:
    print("Recusado. Crédito não aprovado ao cliente por insuficiência de recursos")
elif aprova_emprestimo(vcc,pp,sc) <= 0.29 :
    print("Aprovado. Crédito aprovado ao cliente, requisitos disponíveis")
print (aprova_emprestimo)



print('********** Questão 6 **********')


# Adaptado de: https://novatec.com.br/livros/introducao-python-3ed/
# Escreva uma função que calcule o valor a pagar pelo fornecimento de energia elétrica, a partir da quantidade de KWh consumida e da categoria de uso: 'R' para residências, 'C' para comércios e 'I' para indústrias.
# Calcule o valor de acordo com as regras a seguir:

# Residencial até 500: R$ 0,40 x KWh
# Residencial acima de 500: R$ 0,65 x KWh
# Comercial até 1000: R$ 0,55 x KWh
# Comercial acima de 1000: R$ 0,60 x KWh
# Industrial até 1000: R$ 0,55 x KWh
# Industrial acima de 1000: R$ 0,60 x KWh

# Exemplo de uso da função:
# >>> conta_energia(800,'R')
# 520.0

# COMPLETE-ME
from random import choice
print('De acordo com a investigação da Polícia Cívil do RS, há apenas três tipos de residência em Santa Maria, que David pode estar escondido. Foi apurado que:')
khw = randint(200,1500)
typeOfResidence = ['Residencia','Comercio','Industria']
Residencia = choice(typeOfResidence)
def conta_energia(khw, typeOfResidence):
    if(typeOfResidence == "Residencia"):
        if(khw <= 500):
            return khw * 0.40
        return khw * 0.65
    if(typeOfResidence == "Comercio"):
        if(khw <= 1000):
            return khw * 0.55
        return khw * 0.60
    if(typeOfResidence == "Industria"):
        if(khw <= 1000):
            return khw * 0.55
        return khw * 0.60
        
    
    
print('David tem um(a) {} ,valor do custo de kHW utilizado por David é {}'R''.format(Residencia, conta_energia(khw,Residencia)))


print('********** Questão 7 **********')

# O código abaixo usa a função `choice` para escolher
# (pseudo)aleatoriamente um dos nomes de uma lista
# Altere o código para:
# - Substituir os nomes ('Fulano', etc.), de forma 
#   que a lista tenha seu nome e de mais 3 colegas
# - Caso seu nome não seja o sorteado, mostrar a mensagem
#   'Hoje escapei, amanhã não sei'
from random import choice
print('No filme Jogos Mortais,são selecionados participantes para a execução de jogos macabros onde apenas 1 ou nenhum deles sairá vivo.')
print('Foi organizado um jogo em o participante tem a cabeça enjaulada, e precisa se livrar por um orifício em que se introduz uma chave')
nomes = ['A Professora', 'Artur', 'Gabriel']
escolha = choice(nomes)
print('Que os jogos começem')
print('A chave é encontrada por',escolha,'que consegue sair vivo do jogo')
print('Em uma TV um boneco branco com bochecas vermelhas diz "Hoje',escolha,'escapou, quem sabe em outro dia não"')


print('********** Questão 8 **********')

# Escreva um programa que sorteie 5 vezes um nome
# a partir de uma lista, usando a função choice
# vista no exercício anterior.
# A lista deve incluir seu nome e deve ter pelo
# menos mais 2 nomes.
# O programa deverá contar quantas vezes seu nome foi sorteado
# e mostrar o valor deste contador no final.
print('Meu amigo Lucão saiu com seus amigos Artur,David,Luis e Gabriel por dois dias, bebendo em seu primeiro dia Vodka e Gin ')
from random import choice
lista = ['David','Luis','Artur','Gabriel','Lucão']
contador = 0
x = []
while  (contador<= 20):
  escolha = choice(lista)
  x.append(escolha)
  contador += 1

print('Foram ao todo',contador,'Shots de Vodkca e Gin misturados com gelo de coco, sorteados ordenadamente em uma lista feita por Python no ato, que seu resultado foi',x)

print('{} Tomou  {} shots de Vodkca misturada com Gin'.format('Artur',x.count('Artur')))
print('{} Tomou  {} shots de Vodkca misturada com Gin'.format('David',x.count('David')))
print('{} Tomou  {} shots de Vodkca misturada com Gin'.format('Luis',x.count('Luis')))
print('{} Tomou  {} shots de Vodkca misturada com Gin'.format('Gabriel',x.count('Gabriel')))
print('{} Tomou  {} shots de Vodkca misturada com Gin'.format('Lucão',x.count('Lucão')))
print('Todos passam bem.... Mal')


# CONDICIONAIS.PY #

print('***** Exemplo 1 *****')

tamanho = len('mensagem')
if (tamanho > 10):
  print('Condicao verdadeira!')
print('Continuo executando')
print('Cheguei no final')

print('***** Exemplo 2 *****')

def classifimc(p, h):
  imc = p/h**2
  if imc < 18.5:
    return "Magreza"
  else:
    if imc <= 24.9:
      return "Peso normal"
    else:
      if imc <= 29.9:
        return "Sobrepeso"
      else:
        if imc <= 34.9:
          return "Obesidade grau I"
        else:
          if imc <= 40:
            return "Obesidade grau II"
          else:
            return "Obesidade grau III"

peso = 80
altura = 1.80
print(classifimc(peso,altura))


print('***** Exemplo 3 *****')

def classifimc(p, h):
  imc = p/h**2
  if imc < 18.5:    return "Magreza"
  elif imc <= 24.9: return "Peso normal"
  elif imc <= 29.9: return "Sobrepeso"
  elif imc <= 34.9: return "Obesidade grau I"
  elif imc <= 40:   return "Obesidade grau II"
  else:             return "Obesidade grau III"

peso = 80
altura = 1.70
print(classifimc(peso,altura))


print('***** Exemplo 4 *****')


def classifimc(p, h):
  imc = p/h**2
  if imc < 18.5:
    return "Magreza"
  elif imc <= 24.9:
    return "Peso normal"
  elif imc <= 29.9:
    return "Sobrepeso"
  elif imc <= 34.9:
    return "Obesidade grau I"
  elif imc <= 40:
    return "Obesidade grau II"
  else:
    return "Obesidade grau III"

peso = 80
altura = 1.70
print(classifimc(peso,altura))

# IBGE_CONSULTAS.PY #

# ******************************************************
#  O programa abaixo usa funções e recursos mais
#  avançados de Python. Não se preocupe com o que 
#  você não entende, apenas observe que o programa 
#  também emprega muitos recursos básicos que você 
#  já conhece: import, variáveis, chamada de funções 
#  com um ou mais argumentos, if/else, print e len 
#  (que está explicado em um exercício da aula04)
# ******************************************************

# Obtém a frequência de nascimentos por década para um dado nome
# Documentação: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2
# Este programa não verifica possíveis erros de rede

# Para executar:
# - Não use o botão "Run"
# - Abra a aba "Shell"
# - Digite: python ibge-consulta-nome.py

import requests

name = 'andrea' # substitua o nome!
query = 'http://servicodados.ibge.gov.br/api/v2/censos/nomes/'
response = requests.get(query + name)

if len(response.json()) > 0:
  data = response.json()[0]['res']
  print('Frequência de nascimentos por década para o nome:', name)
  for item in data:
    print(item['periodo'], ":", item['frequencia'])
else:
  print('O IBGE não retornou dados para o nome:', name)
