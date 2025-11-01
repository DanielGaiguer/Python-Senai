import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados_agro.csv', sep=',', encoding='utf-8')

#Quando a bomba é acionada, qual era o nível médio de umidade?
bombaLigada = df[df['bomba_ligada'].isin(['Sim'])]
print(bombaLigada['umidade (%)'])

sns.countplot(x='umidade (%)', data=bombaLigada)
plt.title("Nível médio de umidade")
plt.show()

#Fim

#Existe relação entre luminosidade e temperatura?
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
df.corr(numeric_only=True).unstack().sort_values(ascending=False)
plt.show()

#Sim, existe muita relação entre temperatura de luminiosidade

df['data_hora'] = pd.to_datetime(df['data_hora'])
df['hora'] = df['data_hora'].dt.hour

print(df['hora'])

media_hora = df.groupby('hora')['temperatura (°C)'].mean()

plt.figure(figsize=(10, 6))
plt.plot(media_hora.index, media_hora.values, marker='o', color='orange')
plt.title('Temperatura Média por Hora')
plt.xlabel('Hora do Dia')
plt.ylabel('Temperatura Média (°C)')
plt.grid(True)
plt.show()
