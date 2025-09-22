#EX11
int1 = 5
int2 = 3

print(int1 + int2)

print("\n")
#EX12

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = (nota1 + nota2 + nota3) / 3

print("1° nota: ", nota1)
print("2° nota: ", nota2)
print("3° nota: ", nota3)
print("Média: ", media)

print("\n")

#EX13

idade_usuario = input("Quantos anos você tem? ")
print("A sua idade em meses é: ", int(idade_usuario)*12)
print("\n")

#EX14
primeiro_nome = "Daniel"
sobrenone = "Gaiguer"

print(primeiro_nome + "", sobrenone)

print("\n")

#EX15

adj1 = "linda"
subst1 = "flor"
verbo1 = "cresceu"

print(adj1 + "", subst1 + "", verbo1)
print("\n")

#EX16

idade_usuario = input("Quantos anos você tem?")

if idade_usuario >= 18 : 
    print("Você já pode tirar a CNH!")
else: 
    print("Você ainda não pode tirar a CNH.")

print("\n")

#EX17

senha_correta = "python123"

senha_usuario = input("Digite uma senha: ")

if senha_usuario == senha_correta: 
    print("Login Bem Sucedido")
else: 
    print("Senha Incorreta")

print("\n")

#EX18

num_digitado = input("Digite um número: ")

if num_digitado > 0: 
    print("O número digitado é positivo")
else: 
    print("O número digitado é negativo")

print("\n")

#EX19

num_digitado = input("Digite um número: ")

if (num_digitado % 2) == 0: 
    print("O número digitado é par")
else: 
    print("O número digitado é impar")


print("\n")

#EX20

temperatura = 32

if temperatura > 25: 
    print("Está calor")
elif temperatura > 15 and temperatura < 25 :
    print("Temperatura agradavel")
else:
    print("Está frio")


