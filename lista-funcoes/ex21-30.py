
#EX21

def gerar_mensagens_diarias(lista_nomes):
    for nome in lista_nomes:
        print(f"Bom dia, {nome}! Tenha um ótimo dia!")

nomes = ["Daniel", "João", "Tailene", "Maria", "Ana"]
gerar_mensagens_diarias(nomes)

print("\n")

#EX22

lista_lembretes = ["Jogar", "Estudar Python"]

def adicionar_lembrete(lista_lembretes):
    novo_lembrete = input("Digite um novo lembrete: ")
    lista_lembretes.append(novo_lembrete)
    return lista_lembretes

adicionar_lembrete(lista_lembretes)
adicionar_lembrete(lista_lembretes)

print(f"A sua lista de lembretes atualizada: {lista_lembretes}")

print("\n")

#EX23

def jogar_adivinhacao(numero_secreto):
    numero_digitado = 0 
    while numero_digitado != numero_secreto:
        numero_digitado = int(input("Tente adivinhar o número secreto 0-Para sair: "))
        if numero_digitado == numero_secreto:
            return True
        if numero_digitado == 0:
            return False
        print("Errou, tente novamente")

ganhou = jogar_adivinhacao(5)

if ganhou:
    print("Você Venceu!")
else: 
    print("Que pena, você não acertou!")

print("\n")

#EX26
import random

def gerar_senha(tamanho):
    senha = "".join(random.choice("abcdefghijklmnopqrstuvwxyz123456789") for _ in range(tamanho))
    return senha

tamanho = int(input("Digite a quantidade de caracteres da senha que você deseja criar: "))

print(gerar_senha(tamanho))

print("\n")

#EX27
lista = []
def mostrar_tarefas(lista = []):
    print(lista)

def adicionar_tarefa(lista = []):
    tarefa = input("Insira uma nova tarefa: ")
    lista.append(tarefa)

def remover_tarefa(lista = []):
    if not lista:
        print("Lista vazia!")
        return
    try:
        indice = int(input(f"Digite o índice que deseja remover: (0 a {len(lista)-1}): "))
        removido = lista.pop(indice)
        print(f"Item removido: {removido}")
    except (ValueError, IndexError):
        print("Índice inválido.")

while True:
    escolha = int(input("Escolha entre: \n1) Mostrar lista\n2) Adicionar item\n3) Remover item\n0) Sair\n"))
    if escolha == 1:
        mostrar_tarefas(lista)   
    elif escolha == 2:
        adicionar_tarefa(lista)      
    elif escolha == 3:
        remover_tarefa(lista)
    elif escolha == 0:
        break
    else:
        print("Opção inválida!")
    
print("\n")

#EX28
saldo = 0

def ver_saldo(saldo_atual):
    print(f"Saldo atual: R${saldo_atual}\n")
    return saldo_atual

def depositar(saldo_atual, valor):
    deposito = int(input("Digite o valor do deposito: "))
    valor = deposito
    saldo_atual += valor
    print(f"Deposito concluído!\nSaldo atual: R${saldo_atual}\n")

    return saldo_atual

def sacar(saldo_atual, valor):
    saque = int(input("Digite o valor que deseja sacar: "))
    valor = saque
    if saque <= saldo_atual:
        saldo_atual -= valor
        print(f"Saque concluído! \nValor atual: R${saldo_atual}\n")
    else:
        print("Saldo insuficiente.\n")

    return saldo_atual

while True:
    escolha = int(input("Escolha entre: \n1) Ver saldo\n2) Depositar\n3) Sacar\n"))
    if escolha == 1:
        ver_saldo(saldo)
    elif escolha == 2:
        saldo = depositar(saldo, 0)
    elif escolha == 3:
        saldo = sacar(saldo, 0)
    else:
        break

print("\n")

#EX29
import random

def jogar_par_ou_impar():
    escolha = input("Escolha Par ou Impar: ")
    if escolha not in ["Par", "Impar"]:
        return "Escolha inválida! Escolha entre Par ou Impar."

    for _ in range(1):
        numero = random.randint(1, 10)
        numeroEscolha = int(input("Digite um número: "))
        print(f"O número aleatório gerado foi: {numero}")
        soma = numero + numeroEscolha
        print(f"A soma de {numero} + {numeroEscolha} é: {soma}")
        
        if escolha == "Par" and soma % 2 == 0:
            return "Ganhou!"
        elif escolha == "Impar" and soma % 2 != 0:
            return "Ganhou!"
        else:
            return "Perdeu!"

print (jogar_par_ou_impar())

print("\n")

#EX30
soma = 0
media = 0

def cadastrar_aluno():
    nome = input("Digite seu nome: ")
    nota = []

    for i in range(3):
        while True:
            nota_atual = float(input(f"Digite a {i + 1}ª nota: \n"))
            if 0 <= nota_atual <= 10:
                nota.append(nota_atual)
                break
            else:
                print("A nota deve estar entre 0 e 10.")

    lista_aluno = [nome] + nota
    return lista_aluno

def calcular_media_aluno(lista_aluno):
    notas = lista_aluno[1:]
    media = sum(notas) / len(notas)
    return media

def mostrar_boletim(lista_aluno, media):
    nome = lista_aluno[0]
    notas = lista_aluno[1:]
    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}\n")

todos_os_alunos = []

while True:
    lista_aluno = cadastrar_aluno()
    todos_os_alunos.append(lista_aluno)

    media = calcular_media_aluno(lista_aluno)
    mostrar_boletim(lista_aluno, media)

    outroAluno = input("Deseja cadastrar outro aluno? (s/n): \n")
    if outroAluno != 's':
        break

print("Aqui estão os boletins: \n")
for aluno in todos_os_alunos:
    media = calcular_media_aluno(aluno)
    mostrar_boletim(aluno, media)