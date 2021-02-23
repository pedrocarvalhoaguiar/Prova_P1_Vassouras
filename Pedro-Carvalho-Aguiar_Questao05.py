from time import sleep
import os

def Iniciar():
    while True:
        try:
            agenda = Carregar()
        except:
            agenda = []
    
        print('#------------------------------------------------------#')
        print('#         A G E N D A  D E  E N D E R E Ç O S          #')
        print('#------------------------------------------------------#')
        print('# OPÇÕES                                               #')
        print('# 1 - CADASTRAR NOME                                   #')
        print('# 2 - CONSULTAR NOME                                   #')
        print('# 3 - EXCLUIR NOME                                     #')
        print('# 4 - LISTAR TODOS OS NOMES                            #')
        print('# 5 - ZERAR A AGENDA                                   #')
        print('# 6 - SAIR                                             #')
        print('#------------------------------------------------------#')
        opcao = input(' DIGITE A OPÇÃO DESEJADA (1 A 6): ')
        opcao = ValidarOpcao(opcao)
        if opcao == 1:
            Cadastrar(agenda)
            sleep(2)
        elif opcao == 2:
            Consultar(agenda)
            sleep(2)
        elif opcao == 3:
            Excluir(agenda)
            sleep(2)
        elif opcao == 4:
            Listar(agenda)
            sleep(2)
        elif opcao == 5:
            Zerar(agenda)
            sleep(2)
        elif opcao == 6:
            print('Saindo ...')
            sleep(2)
            print('Obrigado por utilizar os nossos serviços. Até a próxima!')
            break

def Carregar():
    agenda = []
    arquivo = open('agenda.txt', 'r')
    for line in arquivo.readlines():
        colunaInfo = line.split(',')
        contato = {
            'cpf': colunaInfo[0],
            'nome': colunaInfo[1],
            'end': colunaInfo[2],
            'lt': colunaInfo[3],
            'qd': colunaInfo[4],
            'bairro': colunaInfo[5],
            'cidade': colunaInfo[6],
            'uf': colunaInfo[7]
        }
        agenda.append(contato)
    return agenda

def ValidarOpcao(op):
    while op.isalpha(): 
        print('Opção inválida')
        op = input('Digite a opção desejada: ')
    else:
        op = int(op)
        if op > 6 or op < 1:
            print('Opção inválida')
            op = input('Digite a opção desejada: ')
        else:
            return op

def Cadastrar(agenda):
    while True:
        cpf = input('Digite o CPF, sem pontos ou traços: ')
        if not ValidarContato(agenda, cpf):
            break
        else:
            print('Este CPF consta no banco de dados')
    contato = {
        'cpf': cpf,
        'nome': input('Digite o nome: '),
        'end': input('Informe o endereço: '),
        'lt': input('Informe o lote: '),
        'qd': input('Informe a quadra: '),
        'bairro': input('Informe o bairro: '),
        'cidade': input('Informe a cidade: '),
        'uf': input('Informa o Estado: ')
    }    
    agenda.append(contato)
    arquivo = open('agenda.txt', 'a')
    arquivo.write(f'{contato["cpf"]},{contato["nome"]},{contato["end"]},{contato["lt"]},{contato["qd"]},{contato["bairro"]},{contato["cidade"]},{contato["uf"]}\n')
    arquivo.close()
    print('Finalizando o cadastro ...')
    sleep(2)
    print('Endereço adicionado!')


def ValidarContato(agenda, cpf):
    for contato in agenda:
        if contato['cpf'] == cpf:
            return True

def Consultar(agenda):
    print('------- Buscando contato ------')
    if len(agenda) > 0: 
        cpf = input('Digite o CPF para busca: ')        
        if ValidarContato(agenda, cpf):
            for contato in agenda:
                if contato['cpf'] == cpf:
                    print('-'*30)
                    print('Contato encontrado!!!')
                    print('-'*30)
                    MostrarContato(contato)
                    print('-'*30)
                    break
        else:
            print('O CPF digitado não está cadastrado!')
    else:
        print('A lista está vazia! ')

def Excluir(agenda):
    print('------- Excluindo contato ------')
    if len(agenda) > 0: 
        cpf = input('Digite o CPF para exclusão: ')        
        if ValidarContato(agenda, cpf):
            for i, contato in enumerate(agenda):
                if contato['cpf'] == cpf:
                    del agenda[i]
                    break
            arquivo = open('agenda.txt', 'w+')
            for contato in agenda:
                arquivo.write(f'{contato["cpf"]},{contato["nome"]},{contato["end"]},{contato["lt"]},{contato["qd"]},{contato["bairro"]},{contato["cidade"]},{contato["uf"]}\n')
            arquivo.close()
            print('Excluindo ...')
            sleep(2)
            print('Contato excluído!')
        else:
            print('O CPF digitado não está cadastrado!')
    else:
        print('A lista está vazia!')

def Listar(agenda):
    print('Carregando contatos ...')
    sleep(2)
    print('#------------ Lista de contatos ------------#')
    if len(agenda) > 0:
        for i, contato in enumerate(agenda, 1):
            print('-'*30)
            print(f'Contato: {i}\n')
            MostrarContato(contato)            
            print('-'*30)
        print(f'Há {len(agenda)} endereços cadastrados.')
        print('-'*30)
    else:
        print('Não há endereços cadastrados!')  

def Zerar(agenda):
    print('------ Apagar agenda ------')
    if len(agenda) > 0:
        print('1 - Apagar apenas os contatos ')
        print('2 - Excluir o arquivo do sistema ')
        opcao = int(input('DIGITE A OPÇÃO DESEJADA '))
        if opcao == 1:
            arquivo = open('agenda.txt', 'w')
            arquivo.close()
            print('Zerando a agenda ...')
            sleep(2)
            print('Agenda limpa!')
        elif opcao == 2:
            os.remove('agenda.txt')
            print('Excluindo arquivos ...')
            sleep(2)
            print('Exclusão completa!')
    else:
        print('A agenda já está vazia!')
        try:
            agenda = open('agenda.txt')
            agenda.close()
            print('Existe um arquivo vazio, deseja apagá-lo? ')
            print('1 - SIM')
            print('2 - NÃO')
            opcao = int(input('ESCOLHA A OPÇÃO DESEJADA: '))
            if opcao == 1:
                os.remove('agenda.txt')
                print('Excluindo arquivos ...')
                sleep(2)
                print('Exclusão completa!')
            elif opcao == 2:
                print('Arquivo mantido')
                sleep(2)
        except:
            print('Não há agendas no sistema! ')


def MostrarContato(contato):
    print(f'CPF: {contato["cpf"]}, Nome: {contato["nome"]}, Endereço: {contato["end"]}, Lote: {contato["lt"]}, Quadra: {contato["qd"]}\n')
    print(f'Bairro: {contato["bairro"]}, Cidade: {contato["cidade"]}, Estado: {contato["uf"]}')

    
Iniciar()