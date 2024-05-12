r = [7.5, 10, 5, 10, 9.5, 10, 8.5, 6, 10, 9, 5.5, 10, 8.5, 4.5, 5, 7.5, 8, 10, 9, 10, 9.5, 7, 9, 4.5, 9, 9]
w = [5, 7.7, 2.7, 10, 6.7, 10, 8.3, 4, 10, 10, 3, 10, 7.3, 0.7, 0.7, 7, 10, 9, 7.7, 10, 10, 6.7, 10, 5.7, 10, 10]
countr = 0
for i in range(len(r)):
  if  r[i] >= w[i]:
    countr += 1
    
print('Quantos estudantes foram melhor em leitura de código?')
print(countr)
print('************************ Questão 1 ************************')
print('O erro está que countr deve estar fora da função for, estando na linha 3')
print('************************ Questão 2 ************************')
print('A) do programa podemos ver 4 variaveis sendo r,w,countr e i, as variáveis r e w são de uma listagem em formato de listagem em float, já COUNTR e i são variáveis somatórias em INT em que iniciam em 0, ambas.')
print('B) As funções pré-definidas são for,range e if. For utiliza i e r, fato curioso é que len está inserido dentro de range, como um parâmetro e if utiliza r,i e w')
print('C)O operador relacional utilizado é > na linha 5')
print('************************ Questão 3 ************************')
def porcentagem(r,countr):
  return countr/len(r)
print('A porcentagem dos alunos que foram melhor em leitura de código é de',round(porcentagem(r,countr)*100),'%')
print('************************ Questão 4 ************************')


def meanr(r):
  return sum(r)/len(r)

print('a média na prova de leitura de código é',meanr(r))

def meanw(w):
  return sum(w)/len(w)

print('a média na prova de programação foi de',meanw(w))
print('************************ Questão 5 ************************')
print('Vou entregar algumas questões de concurso que envolvam python na próxima semana, fazendo elas e trazendo resultados de no mínimo de 10 questões')
