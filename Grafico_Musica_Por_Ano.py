import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataset.csv')
df['release_date'] = pd.to_datetime(df['release_date'])
df['release_year'] = df['release_date'].dt.year
musicas_por_ano = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x = musicas_por_ano.index, y = musicas_por_ano.values, marker = 'o', color = '#A3D2A3')
plt.title('Número de Músicas por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Músicas')
plt.xticks(np.arange(df['release_year'].min(), df['release_year'].max()+1, 2), size= 8.5)
plt.show()
