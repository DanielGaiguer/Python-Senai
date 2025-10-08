import csv
from datetime import date, datetime, timedelta, time
from collections import Counter, defaultdict
"""
#EX1
#Abrir o arquivo .csv e faz a leitura do mesmo.
with open('vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    #Lê cada linha do arquivo f.
    #delimiter=',': define a vírgula como separador de campos.
    leitor = csv.reader(f, delimiter=',')
    #Pegar o "header" (cabeçalho) do nosso arquivo .csv
    header = next(leitor)
    #Percorre cada linha restante do CSV.
    #Em cada iteração, linha é uma lista de strings, por exemplo ['2025-05-18', 'camisa', '3', '59.90'].
    for linha in leitor:
        #zip(header, linha): Emparelha cada nome de coluna com o valor correspondente da linha, criando pares como ('produto','camisa').
        #dict(...): converte esses pares em um dicionário
        ordem = dict(zip(header, linha))
        # nome do produto                           Preco do Produto
        print('Produto:', ordem['produto'], '| Preço: ', ordem['preco'])

#EX2
somaPreco = 0
with open('vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)
    for linha in leitor:
        ordem = dict(zip(header, linha))
        somaPreco += float(ordem['preco'])
    
    print(f"A soma de todos os valores da coluna Preco é de: {somaPreco:.2f}")
#EX3
totalCompra = 0
with open('vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)
    for linha in leitor:
        ordem = dict(zip(header, linha))
        totalCompra = int(ordem['quantidade']) * float(ordem['preco'])
        print(f"O resultado da transação efetuada no dia {ordem['data']}, foi de R${totalCompra:.2f}")

#EX4

with open('vendas.csv', mode='r', encoding='utf-8', newline='') as f: #Vai abrir o arquivo no modo de leitura
    leitor = csv.reader(f, delimiter=',') #Vai ler cada linha
    header = next(leitor)#ira ler apenas o cabecalho

    with open('vendas_grandes.csv', mode='w', encoding='utf-8', newline='') as f_saida:# Vai abrir o arquivo de saida
        spamwriter = csv.writer(f_saida, delimiter=',')# Vai delimitar a escritura a cada virgula, usando na funcao
        spamwriter.writerow(header)#Vai usar a funcao para escrever o cabecalho

        for linha in leitor:
            ordem = dict(zip(header, linha))#Vai transformar aquela linha em um dicionario
            if int(ordem['quantidade']) > 5:#Caso naquela linha, a quantidade seja maior que 5
                    spamwriter.writerow(linha)#Ele vai escrever no arquivo novo, a linha inteira

#EX5
maiorValor = 0
menorValor = 1000 
with open('vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)

    for linha in leitor:
        ordem = dict(zip(header, linha))
        if float(ordem['preco']) > maiorValor:
            maiorValor = float(ordem['preco'])

        if float(ordem['preco']) < menorValor:
            menorValor = float(ordem['preco'])
    
    print(f'O maior valor lido no arquivo foi de: {maiorValor}')
    print(f'O menor valor lido no arquivo foi de: {menorValor}')

#EX6
produtos = []
with open('vendas.csv', mode='r', encoding='utf-8', newline='')as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)

    for linha in leitor: 
        ordem = dict(zip(header, linha))
        produtos.append(ordem['produto'])#vai jogar todos os produtos dentro de um array para realizar a contagem
    
    maisVendido = Counter(produtos)#vai retornar um objeto, com os produtos que mais apareceram no array

    for produto, qtd in maisVendido.items():
        print(f"O produto {produto}, foi vendido {qtd} vezes")

#EX7
produtos = []
with open('vendas.csv', mode='r', encoding='utf-8', newline='')as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)

    for linha in leitor: 
        ordem = dict(zip(header, linha))
        produtos.append(ordem['produto'])#vai jogar todos os produtos dentro de um array para realizar a contagem
    
    maisVendido = Counter(produtos)#vai retornar um objeto, com os produtos que mais apareceram no array

    print(f"De acordo com os registros, o produto mais vendido foi {maisVendido.most_common(1)[0][0]} com {maisVendido.most_common(1)[0][1]} vendas!")#Esta e a forma de acessar o nome, e a quantidade de vendas do objeto

#EX8

produtos = []
with open('vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)

    for linha in leitor:
        ordem = dict(zip(header, linha))
        produtos.append(ordem['produto'])#Vai jogar todos os produtos dentro do array
    
    maisVendido = Counter(produtos)#Vai contar a quantidade de vezes que cada produto aparece, e criar um dicionario com o produto e o numero de vezes que ele aparece
    soma = defaultdict(int)#Vai criar o objeto de soma, de numeros inteiros
    for produto, qtd in maisVendido.items():#Para cada produto, no dicionario
        soma[produto] += qtd#a soma da chave daquele produto, vai receber a qtd que esta no dicionario, caso nao exista, ira criar uma chave produto com o valor 0

    print(dict(soma))
#EX9
produtos_precos = []
with open('vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)

    for linha in leitor:
        ordem = dict(zip(header, linha))
        produtos_precos.append((ordem['produto'], ordem['preco']))#Vai adicionar ao array, as duas variaveis
    
    agrupado = defaultdict(list)#Vai criar a lista agrupada

    for produto, preco in produtos_precos:
        agrupado[produto].append(preco)#Vai agrupar os precos na chave produto, caso nao exista, e criado caso exista adiciona o valor
        
    print(dict(agrupado))

#EX11

i = 0
with open('vendas.csv', mode='r', encoding='utf-8', newline='')as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)

    for linha in leitor:
        ordem = dict(zip(header, linha))
        while i <= 10: 
            horario = ordem['data']
            formato = '%Y-%m-%d'
            horarioFormatado = datetime.strptime(horario, formato)
            print(f"O horario da venda n{i} é: {horarioFormatado}")
            i += 1


#EX12
i = 0
with open('vendas.csv', mode='r', encoding='utf-8', newline='')as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)

    for linha in leitor:
        ordem = dict(zip(header, linha))

        horario = ordem['data']
        formato = '%Y-%m-%d'
        hoje = date.today()
        horarioFormatado = datetime.strptime(horario, formato)
        diferencaTempo = hoje - horarioFormatado.date()
        print(f"A diferença de data entre a compra na data {horarioFormatado.date()}, na data de hoje é de {diferencaTempo.days} dias")

#EX13

with open('vendas.csv', mode='r', encoding='utf-8', newline='')as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)
    qtdVendasMes = defaultdict(int)

    for linha in leitor:
        ordem = dict(zip(header, linha))

        horario = ordem['data']
        formato = '%Y-%m-%d'
        horarioFormatado = datetime.strptime(horario, formato)
        mes_ano = horarioFormatado.date().strftime("%m-%Y")
        qtdVendasMes[mes_ano] += 1

    for mes, qtd in qtdVendasMes.items():
        print(f"No mês {mes} foi feito {qtd} vendas.")

#EX14
"""
with open('vendas.csv', mode='r', encoding='utf-8', newline='')as f:
    vendasMarco = []
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)
    qtdVendasMes = defaultdict(int)

    for linha in leitor:
        ordem = dict(zip(header, linha))

        horario = ordem['data']
        formato = '%Y-%m-%d'
        horarioFormatado = datetime.strptime(horario, formato)
        mes_ano = horarioFormatado.date().strftime("%m-%Y")
        qtdVendasMes[mes_ano] += 1
        if mes_ano == '04-2025':
            vendasMarco.append(linha)

    print(f"As vendas realizadas no mês de Março foram: {vendasMarco}")