"""

#EX1
try:
    with open('saudacao.txt', 'w') as arquivo:
        arquivo.write("Olá, mundo da programação!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#EX2
try:
    with open('compras.txt', 'x') as arquivo:
        arquivo.write("- Arroz\n- Feijão\n- Macarrão\n- Tomate\n- Alface")
except FileExistsError:
    print("O arquivo 'compras.txt' já existe. Não será sobrescrito.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#EX3
try:
    with open('compras.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except Exception as e:   
    print(f"Ocorreu um erro: {e}")

#EX4

try:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    with open('perfil.txt', 'x') as arquivo:
        arquivo.write(f"{nome}\n{idade}")
except FileExistsError:
    print("O arquivo 'perfil.txt' já existe. Não será sobrescrito.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#EX5
try:
    perfil = {}
    with open('perfil.txt', 'r') as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(": ")
            perfil[chave] = valor
    print(f"Seu nome é {perfil['Nome']} e você tem {perfil['Idade']} anos.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#EX6

try:
    with open('lembretes.txt', 'a') as arquivo:
        while True:
            lembrete = input("Digite um lembrete (ou 'sair' para terminar): ")
            if lembrete.lower() == 'sair':
                break
            arquivo.write(lembrete + '\n')
            print("Lembrete adicionado.")
except FileNotFoundError:
    print("O arquivo 'lembretes.txt' não foi encontrado, criando-o um novo arquivo.")
    with open('lembretes.txt', 'w') as arquivo:
        arquivo.write("")
except Exception as e:
    print(f"Ocorreu um erro: {e}")



#EX7
import datetime
try:
    with open('diario.txt', 'a') as arquivo:
        entrada = input("Escreva sua entrada no diário: ")
        data = str(datetime.datetime.now())
        arquivo.write(f"Data: {data} \n {entrada} \n\n")
        print("Entrada adicionada ao diário.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#EX8
try:
    with open('lembretes.txt', 'r') as arquivo:
        print(arquivo.readline())
except Exception as e:
    print(f"Ocorreu um erro: {e}")
#EX9

lista_diario = []
try:
    with open('diario.txt', 'r') as arquivo:
        #conteudo = arquivo.read()
        for linha in arquivo:
            lista_diario.append(linha)
except Exception as e:
    print(f"Ocorreu um erro: {e}")

print(lista_diario)

#EX10

try:
    with open('compras.txt', 'r') as arquivo:
        for linha in arquivo:
            print(f"{linha.strip()} - concluído")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#EX11

try:
    with open('saudacao.txt', 'w') as arquivo:
        arquivo.write("Olá, mundo da programação!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#EX12


try:
    with open('cadastro.csv', 'w') as arquivo:
        arquivo.write(input("Digite seu nome:"))
        arquivo.write(", ")
        arquivo.write(input("Digite seu email:"))
except FileNotFoundError:
    print("O arquivo 'cadastro.csv' não foi encontrado, criando-o um novo arquivo.")
    with open('cadastro.csv', 'w') as arquivo:
        arquivo.write("")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#EX13

lista_vendas =  ['produto A, 100', 'produto B, 250']
try:
    with open("vendas.txt", 'w') as arquivo:
        for venda in lista_vendas:
            arquivo.write(venda + '\n')
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#EX14 

try:
    with open('vendas.txt', 'r') as arquivo:
        total_vendas = 0
        for linha in arquivo:
            produto, valor = linha.strip().split(', ')
            total_vendas += float(valor)
    print(f"Total de vendas: R$ {total_vendas:.2f}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#EX15
try:
    with open('buscas.log',  'a') as arquivo:
        termo = input("Digite o termo de busca: ")
        arquivo.write(termo + '\n')
        print("Termo de busca registrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


#EX16
try:
    input_arquivo = input("Digite o nome do arquivo a ser lido: ")
    with open(input_arquivo, 'r') as arquivo:
        print(f"O arquivo {input_arquivo} existe")
except FileNotFoundError:
    print(f"O arquivo {input_arquivo} não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#EX17

with open('numeros.txt', 'x') as arquivo:
    arquivo.write("10\n0")

try:
    with open ('numeros.txt', 'r') as arquivo:
        numeros = arquivo.readlines()
        num1 = int(numeros[0].strip())
        num2 = int(numeros[1].strip())
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

#EX18

try:
    with open('dados_secretos.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo 'dados_secretos.txt' não foi encontrado.")
except Exception as e:   
    print(f"Ocorreu um erro: {e}")

#EX19
soma = 0
try:
    with open('valores.txt', 'r') as arquivo:
        for numero in arquivo:
            try:
                soma += int(numero.strip())
            except ValueError:
                print(f"Erro: '{numero.strip()}' não é um número válido.")
    print(f"A soma dos valores é: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

print(f"A soma dos valores é: {soma}")

"""
#EX20
nova_tarefa = ""
lista_tarefas = []
try:
    with open('tarefas.txt', 'r') as arquivo:
        print("Tarefas:")
        for linha in arquivo:
            lista_tarefas.append(linha.strip())
        print(lista_tarefas)
except FileNotFoundError:
    print("O arquivo 'tarefas.txt' não foi encontrado, criando-o um novo arquivo.")
    with open('tarefas.txt', 'w') as arquivo:
        arquivo.write("")

try:
    while nova_tarefa != "sair":
        nova_tarefa = input("Digite uma nova tarefa (ou 'sair' para terminar): ")
        if nova_tarefa.lower() == 'sair':
            break
        lista_tarefas.append(nova_tarefa)
    with open('tarefas.txt', 'w') as arquivo:
        for tarefa in lista_tarefas:
            arquivo.write(tarefa + '\n')
except Exception as e:
    print(f"Ocorreu um erro: {e}")

with open('tarefas.txt', 'r') as arquivo:
    print("Tarefas atualizadas:")
    for linha in arquivo:
        print(linha.strip())