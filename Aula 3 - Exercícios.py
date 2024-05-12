from random import randint


print('********** PARTE 1 **********')

"""
Escreva abaixo um programa que:
- Mostre a mensagem "Estou estudando programação em Python"
- Gere um número inteiro entre 1 e 2, armazenando-o em uma variável
- Se o número for igual a 1, mostre a mensagem "Vou fazer mais exercícios"
- Se o número for igual a 2, mostre a mensagem "Vou consultar o material de apoio"
"""

print( "Estou estudando programação em Python")
from random import randint
n = randint(1,2)
if n == 1:
  print ("Vou fazer mais exercícios")
if n == 2:
  print ("Vou consultar o material de apoio")



print('********** PARTE 2 **********')

"""
Escreva abaixo um programa que:
- Gere 4 números entre 1 e 100, armazenando-os em variáveis nomeadas a, b, c, d
- Calcule a média aritmética entre a, b, c usando a função que você definiu na aula anterior
  (copie e cole a função para o arquivo desta aula)
- Calcule a média aritmética entre b, c, d  
- Use a função `print` duas vezes para mostrar os números sorteados e as médias calculadas
  (uma vez para a b c e outra vez para b c d)

A saída do programa deve ser exatamente no formato exemplificado abaixo, só
com números diferentes a cada execução:
  Média entre 83 54 48 igual a 61.666666666666664
  Média entre 54 48 9 igual a 37.0
"""
from random import randint
b = randint(1,100)
a = randint(1,100)
c = randint(1,100)
d = randint(1,100)
def mean(a,b,c):
  return (a+b+c)/3
print(mean(a,b,c))
def mean2(b,c,d):
  return (b+c+d)/3
print(mean2(b,c,d))






print('********** PARTE 3 **********')

"""
Escreva abaixo um programa que:
- Gere um número inteiro entre 1 e 30 representando um dia
- Armazene o número em uma variável
- Se o número for menor ou igual a 15, mostre a mensagem "Primeira quinzena". 
  Em caso contrário, mostre a mensagem "Segunda quinzena".
"""
from random import randint
dia = randint(1,30)
dia = n
if n >= 15:
  print("Primeira quinzena")
if n <= 15:
  print("Segunda quinzena")


print('********** PARTE 4 **********')


"""
Escreva abaixo um programa que:
- Gere 5 números inteiros positivos em intervalos variados à sua escolha
- Armazene os números em variáveis com nomes à sua escolha
- Use uma variável contadora que é incrementada a cada vez que um dos números gerados for par
- Use a definição de função `mumeropar(n)` fornecida abaixo
- Use a funçãp `print` para mostrar a quantidade de números pares gerados

A saída deste programa deve ser exatamente neste formato a seguir, mas com 
números diferentes a cada execução:
  Quantidade de números pares: 1
"""
from random import randint
a = randint(1,10)
b = randint(1,20)
c = randint(1,50)
d = randint(1,30)
e = randint(1,40)

def numeropar(n):
  if n%2 == 0:
    return True
  else:
    return False

print(a, numeropar(a))
print(b, numeropar(b))
print(c, numeropar(c))
print(d, numeropar(d))
print(e, numeropar(e))

print('********** PARTE 5 **********')

"""
Escreva abaixo um programa que:
- Complete a função chamada `temfebre` para retornar "sim' ou "não" após
  verificar se uma dada temperatura corporal representa febre (veja instruções mais abaixo)
- Gere 2 números fracionários representando temperaturas entre 35 e 40, arredondando-os
  com 1 casa decimal e armazenando-os em variáveis
- Use a função `temfebre` com as temperaturas geradas
- Use a função `print` para compor a saída do programa

A saída deste programa deve ser exatamente neste formato a seguir, adaptado
conforme os números gerados:
  Temperatura: 39.8 Tem febre? sim
  Temperatura: 36.9 Tem febre? não
"""
from random import randint
t = randint(35,40)
x = randint(35,40)

def temperatura(t):
  if t >= 38:
    return "Você está com febre"
  if t == 37:
    return "Você está Bem"
  if t <= 36:
    return "Você está com Hipotermia"
def temperatura(x):
  if t >= 38:
    return "Você está com febre"
  if t == 37:
    return "Você está Bem"
  if t <= 36:
    return "Você está com Hipotermia"

print(temperatura(t))
print(temperatura(x))

print('********** PARTE 6 **********')

"""
Escreva abaixo um programa que auxilia na distribuição de estudantes em grupos:

1. Complete a função chamada `grupos(n, tam)`, que recebe um número de estudantes `n` e
  um número `tam` representando uma quantidade desejada de estudantes por grupo
  - A função deve retornar o número de grupos formados dividindo-se `n` por `tam`
  - Caso a divisão não seja exata, um dos grupos poderá ter menos que `tam` integrantes
  - Por exemplo: n=36, tam=4, grupos=9; n=37, tam=4, grupos=10
  - Dica: O operador `//` será útil neste exercício

2. Complete o restante do programa:
- Gere um número inteiro entre 30 e 40, representando o número de alunos `n`
- Gere um número inteiro entre 3 e 5, representando `tam`
- Use a função `grupos` para obter o número de grupos formado
- Mostre os dados na tela conforme o modelo abaixo, adaptado conforme os números gerados:
  Número de estudantes: 36
  Quantidade de estudantes por grupo: 4
  Número de grupos calculado: 9
"""
from random import randint
n = randint(30,40)
tam = randint (3,5)
  
def grupos(n,tam):
  return n//tam
print (grupos(n,tam))

print(grupos(36,4))




# COMPLETE a função abaixo 
# (lembre de também remover o caracter #)
# def grupos(n, tam):


print('********** PARTE 7 **********')

"""
Escolha um dos exercícios anteriores e resolva-o novamente abaixo, desta vez
inicializando o gerador de números pseudoaleatórios antes de gerar algum número.
Execute o programa diversas vezes e observe se as saídas desta parte se mantêm as mesmas.
"""

from random import randint

n = randint(30,40)
tam = randint (3,5)
  
def grupos(n,tam):
  return n//tam
print (grupos(n,tam))

print(grupos(36,4))

# EXEMPLOS.PY #

print('********** Exemplo 01 **********')
from random import randint

sorteado = randint(1, 6)
print('Número sorteado:', sorteado)
if sorteado == 6:
  print('Conseguimos o maior número!')
  print('Temos muita sorte!')
print('Fim do programa')

print('********** Exemplo 02 **********')
from random import randint

x = randint(1, 100)
print('Idade:', x)
if x >= 18:
  print('Maior de idade')
if x < 18:
  print('Menor de idade')
print('Fim do programa')

print('********** Exemplo 03 **********')
from random import randint

a = randint(1, 10)
b = randint(1, 10)
print('Valores:', a, b)
if a > b:
  print('Primeiro valor é maior')
if a <= b:
  print('Primeiro valor é menor ou igual')

print('********** Exemplo 04 **********')
from random import randint

def parouimpar(n):
  if n % 2 == 0:
    return "par"
  if n % 2 == 1:
    return "impar"

n = randint(1, 100)
print('O número', n, 'é', parouimpar(n))


print('********** Exemplo 05 **********')
n = 0
print(n)
n = 1
print(n)
n = n + 1
print(n)
