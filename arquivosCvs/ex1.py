import csv

with open('vendas.csv', mode='r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f, delimiter=',')
    header = next(leitor)
    print('Colunas encontradas:', header)
    for linha in leitor:
        ordem = dict(zip(header, linha))
        print('Produto:', ordem['produto'], '| Preço: ', ordem['preco'])
