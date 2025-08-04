import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('dataset.csv')
contagem_idiomas = df['language'].value_counts()
colors = ['#A3D2A3', '#E6B3B3', '#C7E1A6', '#B3E0E0', '#A0D7D7', '#C2C7E1',
                   '#D9E1C3', '#A3C1AD', '#A2D6A6', '#B3E5BB']
plt.pie(contagem_idiomas,
        labels=contagem_idiomas.index,
        autopct='%1.1f%%',
        colors=colors,
        shadow= True,
        explode= [0.11, 0.1, 0.05, 0, 0, 0, 0],
        startangle= 70
       )
plt.title('Distribuição de Idiomas das Músicas')
plt.axis('equal')
plt.show()