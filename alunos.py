# ORGANIZANDO A LISTA DE ALUNOS POR SEXO E ORDEM ALFABETICA
def sexo (dados):
  for dado in lista_alf:
    if dado['sexo'].upper() == 'FEMININO':
      feminino.append(dado.copy())
    else:
      masculino.append(dado)

def agenda (feminino, masculino):
  if(len(feminino)):
    x = '\nLista das alunas'
    print('-' * len(x))
    print(x)
    print(f'{"NOME":<15}{"IDADE":<10}{"SEXO":<10}')
    for info in feminino:
      print(f'{info["nome"]:<15}{info["idade"]:<10}{info["sexo"]:<10}')
  if(len(masculino)):
    x = 'Lista dos alunos'
    print('-' * len(x))
    print(x)
    print(f'{"NOME":<15}{"IDADE":<10}{"SEXO":<10}')   
    for info in masculino:
      print(f'{info["nome"]:<15}{info["idade"]:<10}{info["sexo"]:<10}')

feminino = []
masculino = []
lista = []
dados = dict()

dados['nome'] = input('Informe o nome ou SAIR para finalizar: ').title()
 
while dados['nome'].upper() != 'SAIR':
  dados['idade'] = int(input('Informe a idade: '))
  dados['sexo'] = input('Informe o sexo: ').title()
  lista.append(dados.copy())
  dados['nome'] = input('\nInforme o nome ou SAIR para finalizar: ').title()
  
lista_alf = sorted(lista, key=lambda x: x['nome'])
sexo(dados)
agenda(feminino, masculino)