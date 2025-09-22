#EX01
""""
while True:
    try:
        idade = int(input("Qual é a sua idade? "))
        break 
    except ValueError:
        print("Idade Inválida, por favor digite um número ")

print("\n")


#EX02

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        break
    except ValueError:
        print("Entrada inválida, por favor digite apenas números.")

print(f"A soma de {num1} e {num2} é igual a {soma}")

print("\n")

#EX03
while True:
    try:
        temp = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (temp * 9/5) + 32
        break
    except ValueError:
        print("Temperatura inválida.")

print(f"A temperatura em Fahrenheit é: {fahrenheit}°F")

print("\n")

#EX04

while True:
    try:
        num = int(input("Digite uma nota de 0 a 10: "))
        if 0 <= num <= 10:
            break
        else:
            print("Nota fora do intervalo válido!")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    else:
        print("Nota válida!")

print("\n")

#EX05


while True:
    try:
        preco = float(input("Digite o preço do produto: R$ "))
    except ValueError:
        print("Preço inválido.")
    else:
        print(f"Preço registrado: R$ {preco:.2f}")
        break


print("\n")

#EX06


while True:
    try:
        numerador = int(input("Digite o numerador: "))
        denominador = int(input("Digite o denominador: "))
        resultado = numerador / denominador
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros.")
    else:
        print(f"O resultado da divisão é: {resultado}")
        break

print("\n")

#EX07

lista = ["Maçã", "Banana", "Uva"]

while True:
    try:
        indice = int(input("Digite o índice do item que deseja acessar (0-2): "))
        print(f"Item selecionado: {lista[indice]}")
    except IndexError:
        print("Índice inválido! Essa posição não existe.")

print("\n")

#EX08

aluno = {"nome": "Leo", "idade": 17}
while True:
    try:
        chave = input("Digite a chave que deseja acessar (nome, idade): ")
        print(f"Valor: {aluno[chave]}")
    except KeyError:
        print(f"Chave {chave}não encontrada.")

print("\n")

#EX09



lista = []
notas = 0
for _ in range(4):
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        lista.append(nota)
    except ValueError:
        print("Nota inválida. Por favor, digite um número.")

try:
    soma = 0
    for nota in lista:
        soma += nota
    media = soma / len(lista)
except ZeroDivisionError:
    print("Nenhuma nota válida foi inserida.")
else:
    print(f"A média das notas é: {media:.2f}")

print("\n")

#EX10


while True:
    try:
        palavra = input("Digite uma palavra: ")
        indice = int(input("Digite o índice: "))
        print(f"A letra na posição {indice} é '{palavra[indice]}'")
    except IndexError:
        print("Posição fora da palavra!")
    except ValueError:
        print("Índice inválido, por favor digite um número.")

print("\n")

#EX11

try:
    usuario = input("Digite o nome de usuário: ")
    senha = int(input("Digite a senha: ")) 
except ValueError:
    print("Senha inválida, deve conter apenas números.")
else:
    print("Login bem-sucedido!")
   
print("\n")

#EX12

try:
    int("abc")
except ValueError:
    print("Erro de conversão: entrada inválida.")
finally:
    print("Processo de relatório finalizado, com ou sem erros.")

print("\n")

#EX13


try:
    print("Baixando arquivo...")
    raise FileNotFoundError("Arquivo não encontrado.")
except FileNotFoundError as e:
    print(f"Erro ao baixar o arquivo: {e}")
else:
    print("Arquivo baixado com sucesso.")
finally:
    print("Limpando recursos.")

print("\n")

#EX14


try:
    divisor = int(input("Digite um número para dividir 100: "))
    resultado = 100 / divisor
except ZeroDivisionError:
    print("LOG: Tentativa de divisão por zero!")
else:
    print(f"Resultado: {resultado}")    
finally:
    print("Processamento de dados encerrado.")
    
print("\n")

#EX15

try:
    num = input("Digite um número: ")
    numInt = int(num)
    if numInt:
        numFloat = float(num)
except ValueError:
    print("Não foi possível converter para número.")

else:
    print(f"O número convertido para float: {numFloat:.2f}")

print("\n")

#EX16


def obter_numero_inteiro_seguro():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            return num
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

numero = obter_numero_inteiro_seguro()
print(f"Número inteiro válido: {numero}")

print("\n")

#EX17

def buscar_info_aluno(dicionario_aluno, chave_info):
    try:
        return dicionario_aluno[chave_info]
    except KeyError:
        return f"Erro: A chave '{chave_info}' não foi encontrada."
    

print(buscar_info_aluno({"nome": "Leo", "idade": 17, "curso": "Python", }, "email"))

print("\n")

#EX18


def fazer_operacao(num1, num2, operacao):
    try:
        if operacao == "soma":
            return num1 + num2
        elif operacao == "subtração":
            return num1 - num2
        elif operacao == "multiplicação":
            return num1 * num2
        elif operacao == "divisão":
            return num1 / num2
        else:
            return "Operação inválida."
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    
print(fazer_operacao(10, 2, "divisão"))

print("\n")

#EX19

"""

usuario_correto = "admin123"
senha_correta = 12345
i = 0

while i < 3:
    try:
        usuario = input("Digite o nome de usuário: ")
        senha = int(input("Digite a senha: "))
        if usuario == usuario_correto and senha == senha_correta:
            print("Login bem-sucedido!")
            break
        else:
            print(f"Usuário ou senha incorretos. {i+1} tentativa(s) restante(s).")
            i += 1
            if i == 3:
                print("Número máximo de tentativas atingido. Acesso bloqueado.")
    except ValueError:
        print("Senha inválida, deve conter apenas números.")
