#EX21

for numero in range(1, 11): 
    print(numero)

print("\n")

#EX22

for numero in range(10, 0, -1): 
    print(numero)

print("\n")


#EX23

for numero in range(1, 11): 
    print(numero, "x 5 = ", numero*5 )

print("\n")

#EX24

lista_frutas = ["banana", "maca", "laranja", "limao"]

for i in range(4): 
    print(lista_frutas[i])

print("\n")

#EX25
soma = 0
for numero in range(101): 
    soma = numero + soma

print(soma)

print("\n")

#EX26

frase = input("Digite uma frase: ")
vezes = input("Digite um número: ")

for _ in range(int(vezes)):
    print(frase)

print("\n")

#EX27

frase = input("Digite uma palavra: ")

for i in range(len(frase)):
    if frase[i] == 'a' or (frase[i] == 'e') or (frase[i] == 'i') or  (frase[i] == 'o') or  (frase[i] == 'u'):
        print(frase)

print("\n")

#EX28

palavra = input("Digite uma palavra para inverter: ")
palavra_invertida = ""

for i in range(len(palavra) - 1, -1, -1):
    palavra_invertida += palavra[i]

print(palavra_invertida)

print("\n")

#EX29

for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("\n")

#EX30

letras = ['p', 'y', 't', 'h', 'o', 'n']
palavra_formada = ""

for letra in letras:
    palavra_formada += letra

print(palavra_formada)
