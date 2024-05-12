print('***** Exercício 01 *****')

# Escreva um programa que peça repetidamente ao usuário 
# para digitar um número inteiro n dentro do 
# intervalo fechado 1 e 20 (use while True e break)
# Depois que obtiver um n válido, o programa deve
# mostrar a música dos elefantes para o número n, 
# conforme o exemplo abaixo
while True:
  char = int(input('Digite quantos elefantes '))
  if char < 0:
    print('Amigo, você não pode matá-los')
  elif char == 0:
    print('Coloque um número valido')
  elif char > 20:
    print('Muitos Elefantes, não temos como controlar')
  else:
      for n in range(char+1):
        if n == 0:
          print('')
        elif n == 1:
          print('1 elefante incomda muita gente')
        elif n!= 1 and n%2 ==1:
          print(n,'elefantes incomodam muita gente')
        elif n%2 == 0:
          print(n,'elefantes'+'incomodam,'*n +'incomodam muito mais')
  break
    
  
# Exemplo de execução:
# Digite n: -1
# Precisamos de elefantes. Digite novamente.
# Digite n: 99
# Muitos elefantes. Digite novamente.
# Digite n: 0
# Precisamos de elefantes. Digite novamente.
# Digite n: 6
# 1 elefante incomoda muita gente
# 2 elefantes incomodam, incomodam muito mais
# 3 elefantes incomodam muita gente
# 4 elefantes incomodam, incomodam, incomodam, incomodam muito mais
# 5 elefantes incomodam muita gente
# 6 elefantes incomodam, incomodam, incomodam, incomodam, incomodam, incomodam muito mais



#============================================#

print('***** Exercício 02 *****')

# Escreva um programa que gere um arquivo nomeado
# "tabuadas.txt", contendo 10 tabelas de multiplicação,
# sendo a primeira para o número 1, a segunda para o 2, 
# e assim por diante. Cada tabela deve multiplicar o 
# número por 1, 2, até 10, 
# colocando um resultado por linha.
# Você pode formatar as tabelas como preferir.
for n in range(1,11):
  print('Tabuada do {}'.format(n))
  for x in range(1,11):
    print(n,'x',x,'=',n*x)
# Exemplo (início do arquivo, tabuadas do 1 e 2):
# Tabuada do 1:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
# Tabuada do 2:
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

#=========================================#

print('***** Exercício 03 *****')

# Neste exercício, você vai completar a função
# decompoe(valor,cedulas). 
# Esta função deve receber um valor inteiro positivo 
# e uma lista de cédulas do sistema monetário de um país 
# (por exemplo, real, euro, dolar)
# Esta lista de cédulas estará em ordem decrescente 
# (da maior para a menor cédula).
# Como resultado, a função deve retornar uma lista
# com strings indicando a quantidade de cédulas de 
# cada valor. Cédulas não usadas (0 cédulas) ficam
# de fora do resultado. Caso não seja possível decompor
# todo o valor em cédulas, a última string na lista
# deve indicar apenas que serão usadas moedas 
# (não é necessário calcular quantas).


      
    
        
    
      
      
      
    
# Para testar sua função, descomente o código 
# no final deste arquivo

# Exemplo de uso
# reais = [200,100,50,20,10,5,2] 
# euros = [500,200,100,50,20,10,5]
# dolares = [100,50,20,10,5,2,1]
# decompoe(65, reais)
# ['1 de 50', '1 de 10', '1 de 5']
# decompoe(66, euros)
# ['1 de 50', '1 de 10', '1 de 5', 'e moeda(s)']
# decompoe(66, dolares)
# ['1 de 50', '1 de 10', '1 de 5', '1 de 1']

def decompoe(valor, cedulas):
  quantidade =[]
  for n in cedulas:
    notas = valor//n
    quantidade.append(notas)
    valor -= n*notas

  return quantidade




reais = [200,100,50,20,10,5,2] 
euros = [500,200,100,50,20,10,5]
dolares = [100,50,20,10,5,2,1]
while True:
  valor = int(input('Digite um valor: '))
  if (valor <= 0):
    break
  print(decompoe(valor, reais))
  print(decompoe(valor, euros))
  print(decompoe(valor, dolares))

#===============================================#

print('***** Exercício 04 *****')

# Nesta página há exemplos de códigos em Python que usam recursão:
# https://vegibit.com/python-recursion-examples/
# Um destes códigos é de uma função chamada `power`, que
# está reproduzida mais abaixo.
# Estude o código desta função e execute o programa.

# Depois de estudar o código, crie uma função chamada 
# `newpower`, que produza o mesmo resultado da função recursiva, 
# mas sem usar recursão.

def power(num, topwr):
  if topwr == 0:
    return 1
  else:
    return num * power(num, topwr - 1)

def newpower(num, topwr):
  if newpower == 1:
    return 1
  else:
    return num ** (topwr)
  

  
print('{} to the power of {} is {}'.format(4, 7, power(4, 7)))
print('{} to the power of {} is {}'.format(2, 8, power(2, 8)))
print('{} to the power of {} is {}'.format(4, 7, newpower(4, 7)))
print('{} to the power of {} is {}'.format(2, 8, newpower(2, 8)))


#===============================================#

print('***** Exercício 05 *****')

# O coeficiente de correlação de Pearson (r) é uma medida
# de associação linear entre variáveis. 
# Dados n valores medidos para 2 variáveis X e Y, o coeficiente
# de correlação de Pearson entre X e Y é dado pela fórmula 
# apresentada em
# https://pt.wikipedia.org/wiki/Coeficiente_de_correla%C3%A7%C3%A3o_de_Pearson
# Essa fórmula requer o cálculo da média de X e da média de Y, além
# de somatórios para calcular o numerador e o denominador da fórmula

# Complete a função pearson(x,y) abaixo de forma a calcular 
# e retornar o coeficiente de correlação de Pearson para as 
# listas de valores x e y.
# Você pode supor que x e y tenham o mesmo tamanho (não é necessário verificar)

# No final deste arquivo, há um caso de uso desse coeficiente 
# de correlação, buscando medir a associação entre variáveis 
# 'tempo de experiência' e 'salário'.
# Neste exemplo, é usada uma função do módulo scipy.stats.

# Para comparar o resultado de sua função com a função 
# do módulo scipy.stats, descomente o código no final deste arquivo.
# 
# Para saber mais:
# https://www.datacamp.com/tutorial/tutorial-datails-on-correlation

import numpy as np

def pearson(x, y):
  xm = np.mean(x)
  ym = np.mean(y)
  desviox= x - xm
  desvioy = y - ym
  z = np.sum(desviox*desvioy)
  divisor = np.sqrt(np.sum(desviox**2) * np.sum(desvioy**2))
  coefdeparson= z/divisor
  return coefdeparson
  
  

    




import scipy.stats as stats

experience = [1, 3, 4, 5, 5, 6, 7, 10, 11, 12, 15, 20, 25, 28, 30,35]

salary = [20000, 30000, 40000, 45000, 55000, 60000, 80000, 100000, 130000, 150000, 200000, 230000, 250000, 300000, 350000, 400000]

corr, _ = stats.pearsonr(experience, salary)
print(corr)


print(pearson(experience, salary))

#===================================================#

print('***** Exercício 06 *****')
import numpy as np
# Adaptado de:
# https://edisciplinas.usp.br/pluginfile.php/5598408/mod_resource/content/2/Programa__o_para_Estudantes_de_Engenharia.pdf

# O arquivo 'notas.txt' contém notas da primeira avaliação 
# de uma turma, uma nota por linha.
# Escreva um programa que leia este arquivo e mostre na tela 
# o seguinte relatório:
# ----------------
# Nota Diferença
# 5.2  -1.2
# 5.2  -1.2
# 9.7   3.3
# 0.6  -5.8
# 5.5  -0.9
# 8.7   2.3
# 9.9   3.5
# ----------------
# Média: 6.4
# Acima da média: 3
# Abaixo da média: 4
def media(texto):
  with open('notas.txt','r') as f:
    soma = []
    for linha in f:
      valor = float(linha.strip())
      soma.append(valor)
  return np.mean(soma)
resultado = media('texto.txt')

print ('Média:',resultado)


  
  
  



# A primeira coluna do relatório tem as notas lidas do arquivo e 
# a segunda coluna representa a diferença 
# entre a nota e a média das notas.
# Notas maiores ou iguais à média contam como "Acima da média" e
# as demais como "Abaixo da média".
# IMPORTANTE: O cálculo de média deve ser feito usando uma função
# que você poderá definir ou importar

# Para formatar os números no relatório, consulte este material
# https://edisciplinas.usp.br/pluginfile.php/5598408/mod_resource/content/2/Programa__o_para_Estudantes_de_Engenharia.pdf
# Pág. 68, Seção 9.5 - Formatação da saída



#=======================================================#

print('***** Exercício 07 *****')

# O código abaixo processa um arquivo CSV composto por 
# duas colunas contendo notas de provas.
# Primeiramente, o arquivo é aberto e lido linha por linha,
# para construir 2 listas x e y com valores de cada coluna.
# Depois de compor as listas, é calculada a média dos valores
# de cada coluna e a correlação de Pearson para as 2 listas.

# Sua tarefa terá 2 partes:
# 1) Adaptar o código para usar o arquivo provas3cols.csv, 
# que tem 3 colunas. A primeira coluna é um código de matrícula, 
# que deve ser ignorado. Seu código modificado deve obter
# as mesmas listas x e y do programa original.
# 2) Depois de ler as listas x e y, calcule alguma outra
# medida estatística à sua escolha.
import csv


def prova3(x):
  with open(x,mode='r') as arq3:
    ler = csv.reader(arq3,delimiter=',')
    linhas = 0
    for coluna in ler:
      if linhas == 0:
        print(f'Matrícula: {"".join(coluna)}')
        linhas += 1
      else:
        print(f'{coluna[0]},{coluna[1]}.')
        linhas += 1

  print(f'lidas {linhas} linhas.')
        
print(prova3('provas2cols.csv'))
# PROVAS2COLS.CSV #
leitura,escrita
7.5, 5
10, 7.7
5, 2.7
10, 10
9.5, 6.7
10, 10
8.5, 8.3
6, 4
10, 10
9, 10
5.5, 3
10, 10
8.5, 7.3
4.5, 0.7
5, 0.7
7.5, 7
8, 10
10, 9
9, 7.7
10, 10
9.5, 10
7, 6.7
4.5, 5.7
9, 10
9, 10
9, 10

# PROVAS3COLS.CSV #
matricula,leitura,escrita
a1, 7.5, 5
a2, 10, 7.7
a3, 5, 2.7
a4, 10, 10
a5, 9.5, 6.7
a6, 10, 10
a7, 8.5, 8.3
a8, 6, 4
a9, 10, 10
a10, 9, 10
a11, 5.5, 3
a12, 10, 10
a13, 8.5, 7.3
a14, 4.5, 0.7
a15, 5, 0.7
a16, 7.5, 7
a17, 8, 10
a18, 10, 9
a19, 9, 7.7
a20, 10, 10
a21, 9.5, 10
a22, 7, 6.7
a23, 4.5, 5.7
a24, 9, 10
a25, 9, 10
a26, 9, 10

# NOTAS.TXT #
5.2
5.2
9.7
0.6
5.5
8.7
9.9
