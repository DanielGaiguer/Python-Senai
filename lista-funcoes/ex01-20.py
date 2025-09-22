#EX1
def saudar_visitante():
    print("Bem-vindo(a) à TechSolutions! Como posso ajudar?")

saudar_visitante()
saudar_visitante()
saudar_visitante()

print("\n")

#EX2

def emitir_som_alarme():
    print("BEEP! BEEP! BEEP! O bolo está pronto!")

emitir_som_alarme()

print("\n")

#EX3

def cartao_boas_festas():
    print("Feliz Natal e um próspero Ano Novo! Que todos os seus desejos se realizem!")

cartao_boas_festas()

print("\n")

#EX4

def executar_danca_robo(): 
    print("Passo para frente! Giro para a esquerda! Balança os braços!")

executar_danca_robo()
executar_danca_robo()

print("\n")

#EX5

def iniciar_nova_rodada():
    print("--- INÍCIO DA NOVA RODADA ---")

print("Preparem-se!")
iniciar_nova_rodada()

print("\n")

#EX6

def preparar_bebida(bebida):
    print(f"Preparando seu(ua) {bebida}...")

preparar_bebida("café")
preparar_bebida("chá")
preparar_bebida("chocolate quente")

print("\n")

#EX7

def saudar_visitante_personalizado(nome):
    print(f"Bem-vindo(a), {nome} Estamos felizes em vê-lo(a)!")

saudar_visitante_personalizado("Ana")
saudar_visitante_personalizado("Bruno")
saudar_visitante_personalizado("Carlos")

print("\n")

#EX8

def enviar_sms(numero_destino, mensagem):
    print(f"Enviando para {numero_destino}: {mensagem}")

enviar_sms("43 984528617", "Olá, esta é a primeira mensagem automática" )
enviar_sms("43 991542686", "Olá, esta é a segunda mensagem automática" )

print("\n")

#EX9

def dobrar_ingrediente(ingrediente, quantidade_original):
    print(f"Para {ingrediente}, use {quantidade_original * 2 } unidades.")

dobrar_ingrediente("farinha", 2)
dobrar_ingrediente("açucar", 0.5)

print("\n")

#EX11

def fazer_suco(fruta):
    return f"Suco de {fruta} fresco!"

meu_suco = fazer_suco("laranja")

print(meu_suco)

print("\n")

#EX12

def verificar_idade(idade_pessoa, idade_minima=12):
    return idade_pessoa > idade_minima

if verificar_idade(15):
    print("Pode entrar!")
else:
    print("Entrada negada!")

print("\n")

#EX13

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

media = calcular_media(7, 8, 6)

print(media)

print("\n")

#EX14

def reais_para_dolar(valor_reais, cotacao_dolar):
    return valor_reais / cotacao_dolar

print(f"{reais_para_dolar(500, 5.42):.2f}")

print("\n")

#EX15

def classificar_numero(numero):
    if numero > 0: 
        return "Positivo"
    elif numero < 0: 
        return "Negativo"
    else:
        return "Zero"

print(classificar_numero(2))
print(classificar_numero(0))
print(classificar_numero(-5))

print("\n")

#EX16

def pedir_e_somar():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1 + num2

print(pedir_e_somar())

print("\n")

#EX17

def cadastrar_usuario():
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    return [nome, idade]

lista = cadastrar_usuario()

print(lista)

print("\n")

#EX18

def calcular_imc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso / (altura ** 2)
    return imc

print(f"Seu IMC é: {calcular_imc():.2f}")

print("\n")

#EX19

def verificar_login(usuario_correto, senha_correta):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    return usuario == usuario_correto and senha == senha_correta

if verificar_login("admin", "1234"):
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos!")

print("\n")
