import matplotlib.pyplot as plt
import numpy as np

# Sanatçı bazlı karşılaştırmalı analiz
x = np.arange(len(df['Sanatçı']))
fig, ax1 = plt.subplots(figsize=(12, 6))
colors = ['skyblue' if artist != "Sanatçı 5" else 'orange' for artist in df['Sanatçı']]
ax1.bar(x - 0.2, df['Views'], width=0.4, label='YouTube Görüntülemeleri', color=colors)

ax2 = ax1.twinx()
ax2.plot(x, df['Danceability'], label='Spotify Dans Edilebilirlik', color='salmon', marker='o', linewidth=2)

for i, value in enumerate(df['Views']):
    ax1.text(x[i] - 0.2, value + 50000, f"{value:,}", ha='center', fontsize=10)

ax1.set_xlabel('Sanatçılar')
ax1.set_ylabel('YouTube Görüntüleme')
ax2.set_ylabel('Spotify Dans Edilebilirlik')
ax1.set_xticks(x)
ax1.set_xticklabels(df['Sanatçı'], rotation=45, ha='center')
plt.title('Sanatçı Bazında YouTube ve Spotify Performansı')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.show()
