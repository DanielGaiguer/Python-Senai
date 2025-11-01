import pandas as pd

# 1. Ler os dados
df = pd.read_csv("feedbacks.csv", sep=',', encoding='utf-8')

# 2. Calcular média de nota por curso
media_por_curso = df.groupby("curso")["nota"].mean()

# 3. Identificar curso com melhor e pior avaliação
melhor_curso = media_por_curso.idxmax()
pior_curso = media_por_curso.idxmin()

# 4. Contar quantas pessoas recomendaram cada curso
recomendacoes = df.groupby(["curso", "recomendaria"]).size().unstack(fill_value=0)
print(recomendacoes)
# 5. Ver quantidade de feedbacks por dia
feedbacks_por_dia = df.groupby("data").size()

# 6. Filtrar só feedbacks negativos (nota <= 2)
feedbacks_negativos = df[df["nota"] <= 2]

# 7. Salvar feedbacks negativos em novo 
feedbacks_negativos.to_csv("feedbacks_negativos.csv", index=False)

# Exibir resultados
print("=== MÉDIA DE NOTA POR CURSO ===")
print(f"{media_por_curso}")
print("\nMelhor curso:", melhor_curso)
print("Pior curso:", pior_curso)

print("\n=== RECOMENDAÇÕES POR CURSO ===")
print(recomendacoes)

print("\n=== QUANTIDADE DE FEEDBACKS POR DIA ===")
print(feedbacks_por_dia)

print("\n=== FEEDBACKS NEGATIVOS ===")
print(feedbacks_negativos.head())
