from CadastroPessoa.lib.interface import *

def arquivoExiste(nome):
    '''
    -> Verifica se o arquivo existe e retorna uma variavel boleana
    :param nome: nome do arquivo recebido por parâmetro
    :return: True ou False
    '''
    try:
        a = open(nome, 'rt') # 'rt' mode ler o texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    '''
    -> Cria um arquivo com o nome recebido pro parâmetro
    :param nome: nome do arquivo recebido por parâmetro
    :return: sem retorno
    '''
    try:
        a = open(nome, 'wt+') # 'wt+' modo escreva um texto, o '+' esse sinal é para, se não existir, ele cria o arquivo.
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        #print(a.read()) # funciona mas não fica visivelmente bonito (José;35)
        for linha in a:
            dado = linha.split(';') # dado será uma lista
            dado[1] = dado[1].replace('\n', '')# comando para tirar o \n
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    '''
    -> Cadastra uma pessoa no arquivo
    :param arq: nome do arquivo
    :param nome: nome da pessoa
    :param idade: idade da pessoa
    :return: sem retorno
    '''
    try:
        a = open(arq, 'at') # 'at' mode adicionar texto no arquivo
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO no momento de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
    finally:
        a.close()
