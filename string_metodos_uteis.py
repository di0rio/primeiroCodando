name = 'cAuA'

print(name.upper())
print(name.lower())
print(name.title())

############################

texto = '    Olá mundo!  '

print(texto.strip()+ '...')
print(texto.rstrip()+ '...')
print(texto.lstrip()+ '...')

#############################

curso = 'Python'

print(curso.center(20))
print(curso.center(20, '@'))

print('-'.join(curso))

print('')

## %s = string
## %d = int
#####foi alterado por chaves = Método format
#####passar o f-string = codigo limpo
nome, idade, profissao, linguagem, saldo, saldo2 = 'Cauã', 16, 'garoto de programa', 'todas', 'Rico', 230000000000

dados = {'nome': 'Cauã',  'idade': 16}

print('Nome: {} Idade: {}.'.format(nome, idade))
print('Nome: {1} Idade: {0}.'.format(idade, nome))
print('Nome: {1} Idade: {0} || Nome: {1} {1}.'.format(idade, nome))
print('Nome: {nome} Idade: {idade}'.format(nome=nome, idade=idade))

print('')

print('Nome: {nome} Idade: {idade}'.format(**dados))

print('')

print(f'Nome: {nome} Idade: {idade}')
print(f'Nome: {nome} Idade: {idade} Saldo:{saldo}')

print(f'Nome: {nome} Idade: {idade} Saldo:{saldo2:50.2f}')

####FATIANDO STRING
print('')
print('FATIANDO STRING')

nombre = 'Cauã dos Santos Diório'
print(nombre[0])
print(nombre[:9])
print(nombre[9:])
print(nombre[9:16])
print(nombre[0:8:3])
print(nombre[:])
print(nombre[:: -1])

####MULTIPLAS STRING
sla = 'caua'

mensagem = f'''
Ola eu sou {sla},
      estou aprendendo a ser sigma,
               ando fazendo mewing.'''
print(mensagem)

#fazer por variaveis + facil
mensagem2 = (
    f'''
================= TIGRINHO ============================

    1 - Botar mais 20
    2 - Apostar a casa
    3 - Perder tudo

========================================================

    Obrigado pelo dinheiro! Volte com mais na próxima.
    '''
)
print(mensagem2)

