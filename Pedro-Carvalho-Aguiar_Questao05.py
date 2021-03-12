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
        print('# 6 - ATUALIZAR A AGENDA                               #')
        print('# 7 - SAIR                                             #')
        print('#------------------------------------------------------#')
        opcao = input(' DIGITE A OPÇÃO DESEJADA (1 A 7): ')
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
            atualizar(agenda)
            sleep(2)
        elif opcao == 7:
            print('Saindo ...')
            sleep(2)
            print('Obrigado por utilizar os nossos serviços. Até a próxima!')
            break

def Carregar():
    agenda = []
    with open('agenda.txt', 'r') as arquivo:
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
        arquivo.close()
        return agenda

def ValidarOpcao(op):
    while op.isalpha(): 
        print('Opção inválida')
        op = input('Digite a opção desejada: ')
    else:
        op = int(op)
        if op > 7 or op < 1:
            print('Opção inválida')
            op = input('Digite a opção desejada: ')
        else:
            return op

"""
        if ValidarContato(agenda, cpf):
            contato = ValidarContato(agenda, cpf)
            temp = open('temp.txt', 'a')
            with open('agenda.txt', 'r') as arquivo:
                for line in arquivo.readlines():
                    l = line.split(',')
                    if len(l) > 0 and contato['cpf'] != l[0]:
                        temp.write(line)
            temp.close()    
            os.remove('agenda.txt')
            os.rename('temp.txt', 'agenda.txt')
        else:
            print('CPF não encontrado! ')
    else:
        print('A lista está vazia! ')


def atualizar(agenda):
    if len(agenda) > 0:
        cpf = leCpf()      
        if ValidarContato(agenda, cpf):
            contato = ValidarContato(agenda, cpf)
            temp = open('temp.txt', 'a')
            with open('agenda.txt', 'r') as arquivo:
                for line in arquivo.readlines():
                    l = line.split(',')
                    if len(l) > 0:
                        if contato['cpf'] == l[0]:
                            line = leContato(contato['cpf'], 2)
                        temp.write(line)
            temp.close()   
            os.remove('agenda.txt')
            os.rename('temp.txt', 'agenda.txt')

def leContato(cpf, op):
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
    if op == 1:
        return contato
    elif op == 2:
        a = ''
        for i in contato:
            a +=  contato[i] + ','
        b = a[:-1]
        b += '\n'
        return b
"""


def Cadastrar(agenda):
    while True:
        cpf = input('Digite o CPF, sem pontos ou traços: ')
        if not ValidarContato(agenda, cpf):
            break
        else:
            print('Este CPF consta no banco de dados')
    contato = leContato(cpf)   
    agenda.append(contato)
    arquivo = open('agenda.txt', 'a')
    salvarContatoNoDisco(contato, arquivo, 1)
    arquivo.close()
    print('Finalizando o cadastro ...')
    sleep(2)
    print('Endereço adicionado!')

def leContato(cpf):
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
    return contato

def salvarContatoNoDisco(contato, arq, op):
    if op == 1:
        arq.write(f'{contato["cpf"]},{contato["nome"]},{contato["end"]},{contato["lt"]},{contato["qd"]},{contato["bairro"]},{contato["cidade"]},{contato["uf"]}'+ '\n')
    elif op == 2:
        arq.write(f'{contato["cpf"]},{contato["nome"]},{contato["end"]},{contato["lt"]},{contato["qd"]},{contato["bairro"]},{contato["cidade"]},{contato["uf"]}')

def ValidarContato(agenda, cpf):
    for contato in agenda:
        if contato['cpf'] == cpf:
            return contato        
    return None

def leCpf():
    cpf = input('Digite o CPF para busca: ')
    return cpf

def Consultar(agenda):
    print('------- Buscando contato ------')
    if len(agenda) > 0: 
        cpf = leCpf()        
        if ValidarContato(agenda, cpf):
            contato = ValidarContato(agenda, cpf)
            MostrarContato(contato)
        else:
            print('O CPF digitado não está cadastrado!')
    else:
        print('A lista está vazia! ')

def Excluir(agenda):
    print('------- Buscando contato ------')
    if len(agenda) > 0: 
        cpf = leCpf()       
        if ValidarContato(agenda, cpf):
            for i, contato in enumerate(agenda):
                if contato['cpf'] == cpf:
                    del agenda[i]
                    break
            arquivo = open('agenda.txt', 'w')
            for contato in agenda:
                salvarContatoNoDisco(contato, arquivo, 2)
            arquivo.close()
            print('Excluindo ...')
            sleep(2)
            print('Contato excluído!')
        else:
            print('O CPF digitado não está cadastrado!')
    else:
        print('A lista está vazia!')

def atualizar(agenda):
    print('------- Buscando contato ------')
    if len(agenda) > 0: 
        cpf = leCpf()       
        if ValidarContato(agenda, cpf):
            for i, contato in enumerate(agenda):
                if contato['cpf'] == cpf:
                    agenda[i] = leContato(cpf)
                    alterado = agenda[i]
                    break
            arquivo = open('agenda.txt', 'w')
            for contato in agenda:
                if contato == alterado:
                    salvarContatoNoDisco(contato, arquivo, 1)
                else:
                    salvarContatoNoDisco(contato, arquivo, 2)
            arquivo.close()
            print('Excluindo ...')
            sleep(2)
            print('Contato atualizado! ')
        else:
            print('O CPF digitado não está cadastrado!')
    else:
        print('A lista está vazia!')

def Listar(agenda):
    print('----- Carregando contatos -----')
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
            with open('agenda.txt', 'w'):
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