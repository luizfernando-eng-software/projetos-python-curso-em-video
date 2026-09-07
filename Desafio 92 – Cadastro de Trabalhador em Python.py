#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos
# anos a pessoa vai se aposentar.

from datetime import datetime

pessoas_cadastradas = {'nome':[],'ano_nascimento':[],'idade':[],'ctps':[],'ano_contratacao':[],'salario':[],'aposentadoria':[]}

cadastrar = 'S'

qnt_pessoas = 1

ano_atual = datetime.now().year

#FUNÇÕES ---------------------------------------------------------------------

def titulo (palavra,espacamento= False):
    if espacamento == False:
        print(f'\033[34;1m+\033[m{"-" * len(palavra)}\033[34;1m+\033[m')
        print(f'{"|"}{palavra}{"|"}')
        print(f'\033[34;1m+\033[m{"-" * len(palavra)}\033[34;1m+\033[m')
    else:
        print(f'{" " * 5}\033[34;1m+\033[m{"-"*len(palavra)}\033[34;1m+\033[m')
        print(f'{" " * 5}{"|"}{palavra}{"|"}')
        print(f'{" " * 5}\033[34;1m+\033[m{"-" * len(palavra)}\033[34;1m+\033[m')

def linhas (espacamento = False):
    if espacamento == False:
        print(f'\033[34;1m{"-" * 50}\033[m')
    else:
        print(f'\n\033[34;1m{"-" * 50}\033[m\n')

#PROGRAMA PRINCIPAL----------------------------------------------------------

titulo('SISTEMA DE CHECAGEM DE APOSENTADORIA',True)

while cadastrar == 'S':

    print()
    linhas()
    titulo(f'{qnt_pessoas}º Cliente')
    print()

    while True: #VALIDAÇÃO DE NOME: --------------------------------------------------------------------
        nome = input('Digite seu nome: ')
        if nome.replace(' ','').isalpha():
            break
        else:
            print(f'\n\033[1;31mERRO: Digite apenas letras...\033[m\n')
            continue
    nome = nome.title()
    nome = nome.strip()

    while True: #VALIDAÇÃO DE ANO DE NASCIMENTO: -------------------------------------------------------
        try:
            ano_nascimento = int(input('Digite seu ano de nascimento: '))
            if ano_nascimento > ano_atual or ano_nascimento < (ano_atual - 130):
                print(f'\n\033[1;31mERRO: Digite um ano de nascimento válido entre (1896 e 2026)...\033[m\n')
                continue
            else:
                break
        except ValueError:
            print(f'\n\033[1;31mERRO: Digite apenas números inteiros...\033[m\n')

    # ADIÇÃO AO DICIONÁRIO: --------------------------------------------------------------------

    idade = ano_atual - ano_nascimento

    pessoas_cadastradas['nome'].append(nome)
    pessoas_cadastradas['ano_nascimento'].append(ano_nascimento)
    pessoas_cadastradas['idade'].append(idade)

    #INPUT CTPS: --------------------------------------------------------------------

    carteira_trabalho = input('Digite o número da CTPS (Não tenho = digite 0): ')

    if carteira_trabalho != '0':
        while True: #VALIDAÇÃO DO ANO DE CONTRATAÇÃO: -------------------------------------------
            try:
                ano_contratacao = int(input('Digite o seu ano de contratação: '))
                if ano_contratacao <  (ano_nascimento + 14) or ano_contratacao > ano_atual:
                    print(f'\n\033[1;31mERRO: Digite um ano de contratação válido entre ({ano_nascimento+14} e {ano_atual})...\033[m\n')
                    continue
                else:
                    break
            except ValueError:
                print(f'\n\033[1;31mERRO: Digite apenas números inteiros...\033[m\n')

        while True: #VALIDAÇÃO DE SALÁRIO: -------------------------------------------------
            try:
                salario = float(input('Digite seu salário: '))
                if salario <= 0:
                    print(f'\n\033[1;31mERRO: Digite um valor de salário maior que 0...\033[m\n')
                    continue
                else:
                    break
            except ValueError:
                print(f'\n\033[1;31mERRO: Digite apenas números (use "." no lugar de ",")...\033[m\n')


        aposentadoria = (ano_contratacao + 35) - ano_nascimento

        pessoas_cadastradas['ctps'].append(carteira_trabalho)
        pessoas_cadastradas['ano_contratacao'].append(ano_contratacao)
        pessoas_cadastradas['salario'].append(salario)
        pessoas_cadastradas['aposentadoria'].append(aposentadoria)


    else:
        pessoas_cadastradas['ctps'].append('Sem dados')
        pessoas_cadastradas['ano_contratacao'].append('Sem dados')
        pessoas_cadastradas['salario'].append('Sem dados')
        pessoas_cadastradas['aposentadoria'].append('Sem dados')

    linhas(True)
    qnt_pessoas += 1

    while True:
        cadastrar = input('Deseja cadastrar mais pessoas (S/N)? ').upper()
        if cadastrar in ('S','N'):
            break
        else:
            print(f'\n\033[1;31mERRO: Digite uma opção válida ("S" ou "N")...\033\n[m')
            continue

linhas(True)

print('Clientes cadastrados:')

for i in range(0, len(pessoas_cadastradas['nome'])):
    print(f'\nDados do {i+1}º Cliente: {"-" * 30}\n')
    print(f'Nome: {pessoas_cadastradas["nome"][i]}')
    print(f'Ano de Nascimento: {pessoas_cadastradas["ano_nascimento"][i]}')
    print(f'Idade: {pessoas_cadastradas["idade"][i]}')

    if pessoas_cadastradas['ctps'][i] != 'Sem dados':
        print(f'CTPS: {pessoas_cadastradas["ctps"][i]}')
        print(f'Ano de contratação: {pessoas_cadastradas["ano_contratacao"][i]}')
        print(f'Idade de aposentadoria: {pessoas_cadastradas["aposentadoria"][i]}')
        print(f'Salário: {pessoas_cadastradas["salario"][i]}')