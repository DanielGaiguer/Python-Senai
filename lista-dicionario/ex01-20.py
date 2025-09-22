"""
#EX01
jogador = {"nome": "neyma", "pontuacao": 200, "nivel": 5}

print(jogador)

print(jogador["pontuacao"])


#EX02


filme = {"titulo": "Interestelar", "diretor": "Christopher Nolan", "ano_lancamento": 2014, "genero": "Ficção Científica"}
print(filme["titulo"])
print(filme["diretor"])
print("\n")


#EX03

funcionario = {"id": 1, "nome": "João", "cargo": "Analista", "salario": 3500.00}
print(funcionario["nome"])
print(funcionario["cargo"])
print("\n")


#EX04

animal_estimacao = {"nome": "Thor", "especie": "Cachorro", "idade": 3, "cor_pelo": "Preto"}
print(animal_estimacao["especie"])
print(animal_estimacao["idade"])
print("\n")


#EX05

receita = {"nome_prato": "Bolo de Cenoura", "tempo_preparo_minutos": 40, "rendimento_porcoes": 8}
print(receita["nome_prato"])
print(receita["tempo_preparo_minutos"])
print("\n")



#EX06

jogador = {"nome": "Heroi", "pontuacao": 1000, "nivel": 1}
jogador["pontuacao"] = 1250
jogador["nivel"] = 2
print(jogador)
print("\n")


#EX07

livro = {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "estoque": 5}
livro["estoque"] += 10
livro["preco"] = 89.90
print(livro)
print("\n")

#EX08

aluno = {"nome": "Mariana", "idade": 17, "curso": "Programação"}
aluno["notas"] = [8.5, 9.0, 7.5]
aluno["curso"] = "Engenharia de Software"
print(aluno)
print("\n")

#EX09

carrinho_item = {"produto": "Camiseta", "preco_unitario": 49.90, "quantidade": 2}
carrinho_item["quantidade"] = 3
carrinho_item["total_item"] = carrinho_item["preco_unitario"] * carrinho_item["quantidade"]
print(carrinho_item)
print("\n")

#EX10

frutas = {"maça": 3.50, "banana": 2.00, "laranja": 4.00}
frutas["maça"] = 3.80
frutas["uva"] = 6.00
print(frutas)
print("\n")

#EX11

perfil = {"nome": "Pedro", "idade": 22, "cidade": "Rio", "email": "pedro@email.com"}
perfil.pop("email")
print(perfil)
print("\n")

#EX12 
produto = {"id": "A123", "nome": "Teclado RGB", "estoque": 10, "marca": "GamerX"}
produto.pop("estoque")
print(produto)
print("\n")

#EX13 
tarefa = {"descricao": "Comprar pão", "prazo": "Hoje", "prioridade": "Alta"}
removido = tarefa.pop("prazo")
print("Prazo removido:", removido)
print(tarefa)
print("\n")

#EX14 
menu_cafe = {"cafe": 5.00, "bolo": 8.00, "suco": 6.50}
if "pao_de_queijo" in menu_cafe:
    print("Pão de queijo disponível!")
else:
    print("Pão de queijo não está no menu.")
print("\n")

#EX15 
pedido = {"id": "P001", "cliente": "Fernanda", "status": "Processando"}
if "status" in pedido:
    print(pedido["status"])
else:
    print("Status do pedido não encontrado.")
print("\n")

#EX16 
convidados = {"Ana": 28, "Beto": 30, "Carla": 25}
for nome in convidados:
    print(nome)
print("\n")

#EX17 
carrinho = {"maça": 2, "leite": 1, "pao": 3}
for item, quantidade in carrinho.items():
    print(f"Item: {item}, Quantidade: {quantidade}")
print("\n")

#EX18 
livro = {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "genero": "Romance"}
for campo, valor in livro.items():
    print(f"Campo: {campo} - Valor: {valor}")
print("\n")

#EX19 
temperaturas = {"seg": 25.5, "ter": 28.0, "qua": 26.2, "qui": 27.5, "sex": 29.1}
for temp in temperaturas.values():
    print(temp)
print("\n")

#EX20 
vendas_mes = {"Janeiro": 12000, "Fevereiro": 15000, "Março": 13500, "Abril": 18000}
for mes, valor in vendas_mes.items():
    print(f"Mês: {mes}, Vendas: R${valor}")
"""