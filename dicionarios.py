# dict ouu:
# EX.:
dados = {'nome': 'caua'}
print(dados['nome'])

dados['nome'] = 'Maria'# para sobrescrever
print(dados['nome'])

# aninhado
contatos = {
    'caua@gmail.com': {'nome': 'caua'},
    'neymar@gmail.com':{'nome': 'neymar'},
    'meci@gmail.com':{'nome': 'meci'},
    'cris@gmail.com':{'nome': 'cris'}
}
nome = contatos['caua@gmail.com']['nome']
print(nome)

# inteirar
for nome, valor in contatos.items():
    print(nome, valor)

###############################################
    
print('')
print('MÉTODOS')

# clear = apagar
# copy = copiar sem ser o msm

#fromkeys
contatos.fromkeys(['telefone']) #cria chaves sem valores
contatos.fromkeys(['telefone'], 'vazio') #cria chaves com valores

# get = acessar valores da chave podendo trazer em argumento {}
# pop = remove a chave {}
# popitem = remove em sequencia
# setdefault  = adiciona chaves diferentes com valores diferentes # caso não exista
# update = add um novo dicionario
# values = retorna todos os valores e chaves

# in = saber se existe uma chave ou não no dicionário || index
resultado = 'cris@gmail.com' in contatos
print(resultado)
resultado = 'cs@gmail.com' in contatos
print(resultado)

# del = tira o valor passando o obj que deseja remover