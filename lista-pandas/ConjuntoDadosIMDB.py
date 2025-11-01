import pandas as pd
# Carregar o dataset
df = pd.read_csv('IMDB Top 250 Movies.csv')
diretores_explodidos = df['directors'].str.split(', ').explode()
diretores_mais_recorrentes = diretores_explodidos.value_counts().head(10)
print("Diretores mais recorrentes:")
print(diretores_mais_recorrentes)

# Qual a média das avaliações?
media_avaliacoes = df['rating'].mean()
print(f"Média das avaliações: {media_avaliacoes:.2f}")

# Quais os filmes mais antigos e mais recentes?
filme_mais_antigo = df.loc[df['year'].idxmin()]
filme_mais_recente = df.loc[df['year'].idxmax()]

print(f"Filme mais antigo: {filme_mais_antigo['name']} ({int(filme_mais_antigo['year'])})")
print(f"Filme mais recente: {filme_mais_recente['name']} ({int(filme_mais_recente['year'])})")

# Qual a média de duração dos filmes?
# Garantir que 'run_time' está como número (em minutos)
# Função para converter uma string no formato 'Xh Ym' para minutos inteiros
def to_minutes(s):
    try:
        h, m = s.split('h')
        return int(h.strip()) * 60 + int(m.replace('m', '').strip())

    except:
        return None

df['run_time'] = df['run_time'].apply(to_minutes).astype(float)

media_duracao = df['run_time'].mean()

# Exibe a média formatada com duas casas decimais
print(f'Média de duração: {media_duracao:.2f} minutos')

# Quantos filmes há por década?
df['decada'] = (df['year'] // 10) * 10
filmes_por_decada = df['decada'].value_counts().sort_index()
print("Quantidade de filmes por década:")
print(filmes_por_decada)

# Qual gênero é mais frequente?

# Corrigir espaços e separar corretamente
df['generos_list'] = df['genre'].str.replace(',\s*', ',', regex=True).str.split(',')

# Explodir a coluna
generos_explodidos = df.explode('generos_list')

# Remover espaços restantes (caso haja)
generos_explodidos['generos_list'] = generos_explodidos['generos_list'].str.strip()

# Contar os gêneros
genero_mais_frequente = generos_explodidos['generos_list'].value_counts()
print("Gênero mais frequente:")
print(genero_mais_frequente.head(10))

# Filmes com mais de 3 horas de duração (180 min)
filmes_longos = df[df['run_time'] > 180][['name', 'year', 'run_time']]
print("Filmes com mais de 3 horas de duração:")
print(filmes_longos)

#Quais são os 10 melhores filmes de acordo com as avaliações? E os 10 piores?
top_10_melhores = df.sort_values(by='rating', ascending=False).head(10)[['name', 'rating']]
top_10_piores = df.sort_values(by='rating', ascending=True).head(10)[['name', 'rating']]

print("Top 10 melhores filmes:")
print(top_10_melhores)

print("\nTop 10 piores filmes:")
print(top_10_piores)

#1.1 Crie uma nova coluna chamada Década (ex: 1990, 2000, 2010...).
# Garantir que a coluna 'year' é numérica
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Criar coluna 'Década'
col_decada=df['decada'] = (df['year'] // 10) * 10

#1.2 Agrupe os filmes por década e mostre quantos filmes há em cada.
filmes_por_decada = df['decada'].value_counts().sort_index()
print(filmes_por_decada)

#1.3 Qual foi a década com mais filmes no Top 250?
decada_mais_filmes = filmes_por_decada.idxmax()
print(f"A década com mais filmes é: {decada_mais_filmes}")

#1.4 Para cada década, calcule a nota média e duração média dos filmes.
resumo_decadas = df.groupby('decada').agg(
    nota_media=('rating', 'mean'),
    duracao_media=('run_time', 'mean'),
    total_filmes=('name', 'count')
).reset_index()
print(resumo_decadas)

#1.5 Salve esse resumo em um novo CSV chamado resumo_decadas.csv.
resumo_decadas.to_csv("resumo_decadas.csv", index=False)

#2.1 Quantos diretores diferentes existem na lista?
# Separar diretores (caso tenha múltiplos por filme, separados por vírgula)
df['directors'] = df['directors'].astype(str)
todos_diretores = df['directors'].str.split(', ')

# Criar uma lista única de diretores
diretores_explodidos = todos_diretores.explode()
qtd_diretores_unicos = diretores_explodidos.nunique()
print(f"Existem {qtd_diretores_unicos} diretores diferentes.")

#2.2 Quais são os 5 diretores mais frequentes (com mais filmes no Top 250)?
df['directors_list'] = df['directors'].str.split(',')
diretores_explodidos = df.explode('directors_list')


diretores_explodidos['directors_list'] = diretores_explodidos['directors_list'].str.strip()


diretores_mais_frequentes = diretores_explodidos['directors_list'].value_counts().head(5)

print("5 diretores mais frequentes:\n", diretores_mais_frequentes)

#2.3 Qual é a nota média dos filmes de cada diretor (exibir só quem tem 3 ou mais filmes)?
# Adiciona uma linha por diretor por filme
df_diretores = df.copy()
df_diretores = df_diretores.assign(directors=df_diretores['directors'].str.split(', '))
df_diretores = df_diretores.explode('directors')

# Agrupar por diretor
notas_por_diretor = df_diretores.groupby('directors').agg(
    qtd_filmes=('name', 'count'),
    nota_media=('rating', 'mean')
).reset_index()

# Filtrar diretores com 3 ou mais filmes
diretores_3_filmes = notas_por_diretor[notas_por_diretor['qtd_filmes'] >= 3]
print(diretores_3_filmes.sort_values(by='nota_media', ascending=False))

#2.4 Qual diretor tem filme mais bem avaliado?
idx_melhor_nota = df['rating'].idxmax()
melhor_filme = df.loc[idx_melhor_nota]
print(f"O diretor do filme mais bem avaliado ({melhor_filme['name']}) é {melhor_filme['directors']} com nota {melhor_filme['rating']}.")

#2.5 Exporte para CSV um ranking com diretor, quantidade de filmes, nota média.
# Salvar ranking de diretores com 3 ou mais filmes
diretores_3_filmes.to_csv("ranking_diretores.csv", index=False)

#3.1 Crie uma coluna chamada Categoria_Duracao com base nas regras:
#Curto se duração < 90 min
#Médio se entre 90 e 150
#Longo se > 150

def categorizar_duracao(duracao):
    if duracao < 90:
        return 'Curto'
    elif duracao <= 150:
        return 'Médio'
    else:
        return 'Longo'

# Aplicar a função
df['Categoria_Duracao'] = df['run_time'].apply(categorizar_duracao)

#3.2 Mostre quantos filmes tem em cada categoria.
categorias = df['Categoria_Duracao'].value_counts()
print("Quantidade de filmes por categoria de duração:")
print(categorias)

#3.3 Qual a nota média de cada categoria?
nota_por_categoria = df.groupby('Categoria_Duracao')['rating'].mean()
print("Nota média por categoria de duração:")
print(nota_por_categoria)

#3.4 Qual categoria é mais comum no Top 250?
categoria_mais_comum = categorias.idxmax()
print(f"A categoria mais comum é: {categoria_mais_comum}")

#4.1 Quantos filmes foram lançados em cada ano?
filmes_por_ano = df['year'].value_counts().sort_index()
print("Quantidade de filmes por ano:")
print(filmes_por_ano)

#4.2 Qual ano teve mais filmes no Top 250?
ano_mais_filmes = filmes_por_ano.idxmax()
print(f"O ano com mais filmes no Top 250 é: {ano_mais_filmes}")

#4.3 Quais os filmes lançados entre 1990 e 1999 com nota acima de 3?
filmes_anos_90 = df[(df['year'] >= 1990) & (df['year'] <= 1999) & (df['rating'] > 3)]
print(filmes_anos_90[['name', 'year', 'rating']])

#4.4 Exporte esses filmes para filmes_anos_90.csv.
filmes_anos_90.to_csv("filmes_anos_90.csv", index=False)

#5.1 Quantos filmes contêm a palavra "Love" no título?
qtd_love = df['name'].str.contains("Love", case=False, na=False).sum()
print(f"Quantidade de filmes com 'Love' no título: {qtd_love}")

#5.2 Liste os filmes que têm a palavra "War", "God" ou "King" no título.
filtro = df['name'].str.contains(r"\b(War|God|King)\b", case=False, na=False)
filmes_war_god_king = df[filtro][['name', 'year', 'rating']]
print("Filmes com 'War', 'God' ou 'King' no título:")
print(filmes_war_god_king)

#5.3 Crie uma nova coluna chamada titulo_maiusculo com os títulos em letras maiúsculas.
df['titulo_maiusculo'] = df['name'].str.upper()
print(df['titulo_maiusculo'])

#5.4 Quantos títulos têm mais de 25 caracteres?
qtd_titulos_longos = df['name'].str.len().gt(25).sum()
print(f"Número de títulos com mais de 25 caracteres: {qtd_titulos_longos}")

#5.5 Qual o título mais longo da lista?
titulo_mais_longo = df.loc[df['name'].str.len().idxmax()]
print(f"Título mais longo: {titulo_mais_longo['name']} ({len(titulo_mais_longo['name'])} caracteres)")

#6.1 Mostre todos os filmes:
#com nota ≥ 8
#com duração ≤ 100
#lançados após o ano 2000

filtro_6_1 = (df['rating'] >= 8) & (df['run_time'] <= 100) & (df['year'] > 2000)
filmes_filtrados_6_1 = df[filtro_6_1][['name', 'year', 'rating', 'run_time']]
print("Filmes com nota ≥ 8, duração ≤ 100 min, lançados após 2000:")
print(filmes_filtrados_6_1)

#6.2 Filtre os filmes que:
#Têm duração entre 120 e 150 minutos
#Foram dirigidos por “Christopher Nolan” Estão entre os 50 primeiros do ranking Exporte o resultado de 9.2 para filmes_nolan.csv.

# Garantir que 'rank' é numérico
df['rank'] = pd.to_numeric(df['rank'], errors='coerce')

filtro_6_2 = (
    (df['run_time'] >= 120) &
    (df['run_time'] <= 150) &
    (df['directors'].str.contains("Christopher Nolan", na=False)) &
    (df['rank'] <= 50)
)

filmes_nolan = df[filtro_6_2][['rank', 'name', 'year', 'rating', 'run_time', 'directors']]
print("Filmes de Christopher Nolan com duração entre 120-150min no Top 50:")
print(filmes_nolan)

filmes_nolan.to_csv("filmes_nolan.csv", index=False)

#6.3 Mostre os filmes com título iniciado pela letra “A” e nota acima de 8.0.

filtro_6_3 = df['name'].str.startswith('A') & (df['rating'] > 8.0)
filmes_com_a = df[filtro_6_3][['name', 'year', 'rating']]
print("Filmes que começam com 'A' e nota > 8.0:")
print(filmes_com_a)

#6.4 Liste todos os filmes que não foram dirigidos por “Steven Spielberg”.
filtro_6_4 = ~df['directors'].str.contains("Steven Spielberg", na=False)
filmes_sem_spielberg = df[filtro_6_4][['name', 'year', 'directors']]
print("Filmes que não foram dirigidos por Steven Spielberg:")
print(filmes_sem_spielberg)
