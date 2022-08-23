def leiaInt(msg):
    '''
        -> Valida se o valor digitado pelo usuario é um número inteiro
        :param msg: Mensagem de solicitação de parâmetro
        :return: retorna o número inteiro digitado pelo usuário
        '''
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite uma opção válida.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[33mO usuário preferio sair sem digitar um valor.\033[m')
            break
        else:
            return n


def lin(tam=42):
    '''
    -> Cria linha do tamanho o parâmetro recebido
    :param tam: comprimento da linha
    :return: a linha no tamnho do paâmetro
    '''
    return '-' * tam


def cabeçalho(msg):
    '''
    -> Recebe uma mensagem e cria um cabeçalho formatado
    :param msg: mensagem recebida
    :return: retorna um cabeça~ho formatado
    '''
    print(lin())
    print(msg.center(42))
    print(lin())


def menu(lista):
    '''
    -> Cria um menu apartir de uma lista recebida
    e recebe a opção digitada.
    Após validar, retorna para o sistema.
    :param lista: lista contendo as opções do menu.
    :return: a opção do menu.
    '''
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(lin())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc



