print('***** Exercício 01 *****')

# Escreva uma função chamada `countchars`,
# que receba uma lista de strings e
# retorne a quantidade total de caracteres na lista
# Você deve usar repetição com for neste exercício

# Exemplo de uso:
# >>> countchars(['Era uma vez', 'Há muitos anos atrás'])
# 31
print('Dentro de uma partida online de league of Legends, JorginhoPoste estava jogando na posição do Topo, em suas duas primeiras mortes foi derrotado em um 1x1 contra o oponente de rota, em sua volta a rota sob condições inferiores ao oponente, seguindo um comportamento suspeito de disputa, é morto novamente.')
print('JorginhoPoste abre o chat e diz:')
list = " - Olha esse gordo filho de uma p** da Augusta... Filhoooo da p**aaa!!!!!Caballo imundo do car***, Rito Gomez da ban, perma ban nele. Pelo amor de Deus cara, pelo amor de Deus. Esse cara é bronze, ota**, lixo filho da p**"
def countchars(list):
  return len(list)
 
print(list)
print('Sob estas {} palavras JorginhoPoste foi banido até o ano 3023'.format(len(list)))

# https://www.youtube.com/watch?v=sAtG0ibWC1g&ab_channel=WorldOfMenes


print('***** Exercício 02 *****')
from random import randint 
# Fonte: https://programming-23.mooc.fi/part-4/4-definite-iteration

# Escreva uma função nomeada `sum_positives`,
# que receba uma lista de inteiros como argumento e
# retorne a soma dos valores positivos na lista.
# Você deve usar repetição com for neste exercício

# Exemplo de uso:
# >>> sum_positives([1, -2, 3, -4, 5])
# 9
sum_positives = 0

for i in range(5):
  i = randint(-100,100)
  if i >= 0:
      sum_positives += i 
      print('n = ',i)
  else:
      print('n = ',i)
print('O resultado é',sum_positives)
# def sum_positives(soma):
#   if 
#   soma += soma1
# print(sum_positives(soma1))


# my_list = [1, -2, 3, -4, 5]
# result = sum_positives(my_list)
# print("The result is", result)
print('***** Exercício 03 *****')
from random import randint
# Escreva uma função chamada `maiordalista`,
# que receba uma lista de números como argumento e
# retorne o maior deles
# Você deve usar repetição com for neste exercício

# Exemplo de uso:
# >>> maiordalista([9, 5, 3, 23, 1, 4])
# 23
lista = []
for i in range(10):
  i = randint(1,100)
  lista.append(i)
def maiordalista(lista):
  max(lista)
print(lista)
print(max(lista))


# lista = [9, 5, 3, 23, 1, 4]
# print(maiordalista(lista))
#=======================================#

print('***** Exercício 04 *****')
from random import randint
# Neste exercício, você vai escrever 2 funções:

# 1) Uma função nomeada `media_aritmetica`,
# que recebe uma lista de números como argumento
# (representando notas de avaliações)
# e retorna a media aritmética desses números
# Você pode usar qualquer estrutura de repetição neste exercício (for, while)


# 2) Uma função chamada `mensagem`,
# que recebe um número representando uma média
# de notas em avaliações, e retorna uma
# string com uma mensagem diferente de acordo
# com uma faixa em que a média se encontra
# (por exemplo, media < 5, media < 7, etc.)
# A função deve produzir pelo menos 3 mensagens
# diferentes, mas você pode definir as faixas
# e o conteúdo das mensagens.
# Por exemplo:
# >>> mensagem(6.5)
# Na trave! Será que vai ser arredondado?
# >>> mensagem(9.5)
# Uau, que baita média!


def media_aritmetica(lista):
  return sum(lista)/len(lista)



def mensagem(media):
  if 5 < media < 7:
    return 'Só o básico'
  elif 8 <= media <= 9:
    return 'Boa cpx'
  elif 9 < media:
    return 'Foi mt bem'
  elif 5 >= media:
    return 'Precisa estudar'



lista = [8, 5, 9, 5]
media = media_aritmetica(lista)
print(mensagem(media))
#===============================#
print('***** Exercício 05 *****')
from random import choice 
from random import randint
# Escreva uma função nomeada `desvio_padrao`
# que receba uma lista de números como argumento
# e retorne o desvio padrão desses números,
# calculado conforme explicado aqui:
# https://mundoeducacao.uol.com.br/matematica/desvio-padrao.htm

# Você deve usar uma estrutura de repetição para
# codificar a função `desvio_padrao`

# Como o desvio padrão depende de um cálculo de média,
# você pode usar aqui a função media_aritmetica
# definida no exercício anterior, ou procurar uma
# biblioteca que ofereça uma função pronta para
# cálculo de média

# No programa que acompanha este exercício,
# você verá que existe uma biblioteca que oferece
# uma função 'pronta' para calcular o desvio padrão
# (statistics.stdev)
# Você vai poder comparar o resultado da sua função
# com o resultado da função stdev (mas obviamente
# não pode usar stdev dentro da sua função!)
x = randint(2,20)
z = 0
lista = []
for x in range(8):
  x = randint(2,20)
  lista.append(x)

def media_aritmetica(lista):
  return sum(lista)/len(lista)


def modulo(lista,media_aritmetica):
  resulta = 0
  print(lista)
  for i in lista:
      resulta += i - media_aritmetica
  return resulta



def desvio_padrao(lista,media_aritmetica,modulo):
  return 0.5**(modulo**2)/len(lista)



print(float(desvio_padrao(lista,media_aritmetica(lista),modulo(lista,media_aritmetica(lista)))))





import statistics

numeros = [2, 4, 4, 4, 5, 5, 7, 9]

dp = statistics.stdev(numeros)
print("O desvio padrão do módulo statistics é:", dp)
dp = desvio_padrao(numeros)
print("O desvio padrão com a minha função é:", dp)
#=================================#
print('***** Exercício 06 *****')

# Adaptado de: https://codingbat.com/prob/p192589
# Escreva uma função sum2 que receba uma lista de inteiros e retorne a soma do primeiro e do último elementos da lista. Caso a lista só tenha um elemento, retorne ele mesmo. Se a lista for vazia, retorne 0.

# Exemplos de uso:
# >>> sum2([1, 2, 3])
# 4
# >>> sum2([1, 1])
# 2
# >>> sum2([1])
# 1
# >>> sum2([])
# 0
# >>> sum2([1, 1, 1, 1])
# 2


  
def sum2(lista):
  print(lista)
  if len(lista) < 2:
    return 0
  else:
    return lista[0] + lista[len(lista)-1]


print(sum2([1, 2, 3]))

  
print(sum2([1, 1]))

  
print(sum2([1]))

  
print(sum2([]))

  
print(sum2([1, 1, 1, 1]))
#=====================================#
print('***** Exercício 07 *****')

# Escreva uma função que receba um número N
# inteiro e positivo e
# que retorne o resultado S da seguinte soma:
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N

# Exemplo de uso:
# >>> serie(8)
# 2.7178571428571425


def serie(N):
  S = 0
  for i in range(N):
    S += 1/(i+1)
  return S

print(serie(8))

#====================================#
print('***** Exercício 08 *****')

# Escreva um programa que mostre na tela uma "pirâmide"
# formada por `n` linhas com caracteres repetidos, como
# no exemplo mais abaixo
# O valor da variável n deve ser atribuído no início do
# programa e o restante do código deve ser escrito
# em função de n (sem usar valores constantes)
# O caracter usado também deve ser atribuído a uma
# variável no início do programa. Para trocar o 
# caracter usado na pirâmide, deve ser suficiente alterar
# o valor da variável que o representa

# Dica: use (sem modificar) a função `replica` que está nos
# exemplos do material de aula 

# Para n = 10
#           *
#          ***
#         *****
#        *******
#       *********
#      ***********
#     *************
#    ***************
#   *****************
#  *******************
# *********************

# def replica(c, n):
#   s = ''
#   for i in range(n):
#     s += c
#   return s

def replica2(n):
  s ='*'
  n = 10
  for i in range(n):
    e = '' * (n-i)
    ss = s * (2*i -1)
    print(e + ss + e)

def replica(c, n):
  s = ''
  for i in range(n):
    s += c
  return s

def triangle(n):
    
    temp = n - 1
    for i in range(0, n):
        for j in range(0, temp):
            print(end=" ")
        
        temp = temp - 1
        for j in range(0, i+1):
            print("* ", end="")
        print('\r')
        # print(replica('*',i))
    
triangle(11)
#=====================================#
print('***** Exercício 09 *****')

# Escreva uma função `only_longs` que
# receba uma lista de strings e
# retorne outra lista contendo somente as
# strings que tenham mais de 3 caracteres



strings=[]
def only_longs(words):
  select_word = []
  for word in words:
    if(len(word) > 3):
      select_word.append(word)
  return select_word



strings = ['O', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'Roma']
print(only_longs(strings))

# def only_longs(words):
#     select_words = []
#     for word in words:
#         if(len(word) > 3):
#             select_words.append(word)
#     return select_words
    
    
    
# print(only_longs(strings))
print('acho que houve um erro do programa, não achei erro no código')

#===========================================#

print('***** Exercício 10 *****')

# Neste exercício, sua tarefa será apenas examinar
# o código deste programa e anotar abaixo tudo que você
# entendeu e/ou não entendeu.
# Procure identificar os recursos de Python que foram vistos
# nas aulas e estão presentes no programa.
# Procure entender as 3 formas diferentes de mostrar a frase
# no final do programa e argumente sobre vantagens / desvantagens
# de cada uma.
# Mesmo que você não consiga entender o programa, anote suas dúvidas.

# ***************************************
print('Escreva suas anotações aqui:')
print('Pipo é um elemento que está conectando a outros elementos descritos sobre as funções dipostas no problema. As linhas 27 - 55 estão preparando a variável para a atribuição de listagem das conexões possiveis dentro da importação aleatoria requirida na linha 24. Ao final da linha 55, está iniciando a função pipo que dentro das três formas disponiveis no problema, utiliza-se elementos diversificados para a formação lógica do programa. Na forma 1, estamos sob a lógica "for" que utiliza-se de uma variavel frase, que de modo inicial encontra-se vazia, consequetemente o "for" vai conectar pelo "append", abaixo de sua constituição, de modo aleatorio por via do choise, inserido sob forma randomica na linha 24. Ao final da função, está o "print" que arraiga dentro de seus parâmetros o "join" que aplica ao final de cada string, um espaço visto no ""''"", construíndo a frase. Na forma 2, está disposto a lógica de concatenação de strings, a ideia de união diversificada dos strings de "pipo". A repetição lógica está na formula de "escolha + espaço e /", a barra é utilizada para continuar a lógica da linha sob outra linha, como uma permissão de passagem. Por final, a lógica da forma 3 é de "{}" que paira sob um ideia de concatenação, "f" está mostrando      , a função choice de caráter randomico escolhe elementos que estarão dispostos nas posições especificas colocadas nos [].')
# ***************************************

# A título de curiosidade...
# Este programa é inspirado neste site:
# http://www.lepipotron.com/
# que serviu de inspiração para este outro:
# https://pipotron.moul.io/

from random import choice

pipo = []
pipo.append(['Com', 'Considerando', 
             'Qualquer que seja', "Enquanto durar"])

pipo.append(['a situação', 'a conjuntura', 'a crise', 
             'a inércia', 'a dificuldade'])

pipo.append([w + ',' for w in [
    'presente', 'atual', 'que nos preocupa', 
    'contemporânea', 'da sociedade', 'dos últimos tempos']
])

pipo.append(['convém', 'é preferível', 'seria interessante', 
             'não podemos deixar de', 'é necessário', 'é urgente'])

pipo.append(['estudar', 'examinar', 'não negligenciar', 
             'levar em consideração',
             'antecipar', 'imaginar', 'relembrar'])

pipo.append(['todas as', 'o conjunto de', 
             'a totalidade de', 'certas', 'algumas'])

pipo.append(['soluções', 'problemáticas', 
             'opções', 'alternativas', 'questões'])

pipo.append([w + '.' for w in [
  'possíveis', 'que se oferecem a nós', 
  'que já possuímos', 'de senso comum',
  'previsíveis']
])

# Forma 1: construindo a frase com for
frase = []
for p in pipo:
  frase.append(choice(p))
print(' '.join(frase))

# Forma 2: construindo a frase com operador '+' de concatenação de strings
frase = choice(pipo[0]) + ' ' + \
  choice(pipo[1]) + ' ' + \
  choice(pipo[2]) + ' ' + \
  choice(pipo[3]) + ' ' + \
  choice(pipo[4]) + ' ' + \
  choice(pipo[5]) + ' ' + \
  choice(pipo[6]) + ' ' + \
  choice(pipo[7])
print(frase)

# Forma 3: construindo a frase com f-strings 
# (uma das muitas formas de formatar strings em Python)
# Veja mais sobre formatação de strings em Python aqui:
# https://algoritmosempython.com.br/cursos/programacao-python/strings/
frase = f"{choice(pipo[0])} {choice(pipo[1])} {choice(pipo[2])} {choice(pipo[3])} {choice(pipo[4])} {choice(pipo[5])} {choice(pipo[6])} {choice(pipo[7])}"
print(frase)
