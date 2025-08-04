import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataset.csv')
plt.figure(figsize=(10,6))
sns.histplot(df['duration'], bins=30, kde=True, color='#24C06A')
plt.title('distribuicao de duracao das musicas')
plt.xlabel('Duração (segundos)')
plt.ylabel('Frequência')
plt.show()