import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('dataset.csv')
colors = ['#A3D2A3', '#E6B3B3', '#C7E1A6', '#B3E0E0', '#A0D7D7', '#C2C7E1',
                   '#D9E1C3', '#A3C1AD', '#A2D6A6', '#B3E5BB']
label = df.label.value_counts()

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
ax3 = sns.barplot(x = label.index, y = label.values,  palette=colors)
for container in ax3.containers:
    ax3.bar_label(container, fmt='%d', label_type='edge', fontsize=9, color='black', padding=2)
ax3.set(xlabel = 'Produtoras', ylabel = 'Número de Músicas')
plt.title('Distribuição de Músicas por Produtora')
plt.show()
