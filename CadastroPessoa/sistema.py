'''O programa é um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''
from CadastroPessoa.lib.interface import *     # O "*" quer dizer que estamos importando tudo
from CadastroPessoa.lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de ler o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção para cadastrar uma nova pessoa
        cabeçalho('NOVE CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção para sair do programa
        print(lin())
        print('\033[33mSaindo do programa...', end=' ')
        sleep(2)
        print('Até logo!\033[m')
        print(lin())
        break
    else:
        # Digitou uma opção errada
        print('\033[31mERRO: Por favor, digite uma opção válida.\033[m')
    sleep(2)
