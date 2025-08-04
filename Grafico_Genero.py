import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset.csv')
genero_contagem = df.genre.value_counts()
colors = ['#A3D2A3', '#E6B3B3', '#C7E1A6', '#B3E0E0', '#A0D7D7', '#C2C7E1',
                   '#D9E1C3', '#A3C1AD', '#A2D6A6', '#B3E5BB']
plt.figure(figsize=(10, 6))
plt.pie(genero_contagem,
        labels=genero_contagem.index,
        autopct='%1.1f%%',
        colors=colors,
        shadow= True,
        explode= [0.07, 0.07, 0.07, 0, 0, 0, 0, 0, 0]
       )
plt.title('Distribuição de Gêneros Musicais')
plt.axis('equal')
plt.show()