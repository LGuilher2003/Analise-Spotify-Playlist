import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataset.csv')
colors = ['#A3D2A3', '#E6B3B3', '#C7E1A6', '#B3E0E0', '#A0D7D7', '#C2C7E1',
                   '#D9E1C3', '#A3C1AD', '#A2D6A6', '#B3E5BB']
top_artistas = df.groupby('artist').size().reset_index(name='song_count')
top_artistas = top_artistas.sort_values(by='song_count', ascending=False).head(10)
plt.figure(figsize=(12, 6))
ax1 = sns.barplot(x = 'artist', y = 'song_count', data =  top_artistas, palette=colors)
for container in ax1.containers:
    ax1.bar_label(container)
plt.title('Top 10 Artistas Mais Ouvidos')
plt.xlabel('Artistas')
plt.ylabel('Número de Músicas')
plt.show()