import matplotlib.pyplot as plt
import numpy as np

# YouTube ve Spotify karşılaştırmalı popülerlik analizi
x = np.arange(len(youtube_top_tracks))
width = 0.35

fig, ax = plt.subplots(figsize=(14, 8))
ax.bar(x - width/2, youtube_top_tracks["Views"], width, label='YouTube İzlenme', color='skyblue')
ax.bar(x + width/2, spotify_top_tracks["Danceability"], width, label='Spotify Dans Edilebilirlik', color='salmon')

ax.set_xticks(x)
ax.set_xticklabels(youtube_top_tracks["Artist"] + " - " + youtube_top_tracks["Title"], rotation=45, ha="right")
ax.set_title("YouTube ve Spotify Şarkı Popülerliği Karşılaştırması")
ax.set_xlabel("Şarkılar")
ax.set_ylabel("İzlenme / Dans Edilebilirlik Skoru")
ax.legend()

plt.tight_layout()
plt.show()
