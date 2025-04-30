import matplotlib.pyplot as plt

# Grafikler için 3 bar grafiği alt alta çiziliyor
fig, axes = plt.subplots(3, 1, figsize=(12, 18))

# En çok görüntüleme alan sanatçılar
axes[0].bar(top_views["Artist"], top_views["Views"], color="skyblue", edgecolor="black")
axes[0].set_title("En Çok Görüntüleme Alan Sanatçılar", fontsize=16)
axes[0].set_xlabel("Sanatçılar", fontsize=12)
axes[0].set_ylabel("Görüntüleme Sayısı", fontsize=12)
axes[0].tick_params(axis='x', rotation=45)

# En çok beğeni alan sanatçılar
axes[1].bar(top_likes["Artist"], top_likes["Likes"], color="salmon", edgecolor="black")
axes[1].set_title("En Çok Beğeni Alan Sanatçılar", fontsize=16)
axes[1].set_xlabel("Sanatçılar", fontsize=12)
axes[1].set_ylabel("Beğeni Sayısı", fontsize=12)
axes[1].tick_params(axis='x', rotation=45)

# En fazla yorum yapılan sanatçılar
axes[2].bar(top_comments["Artist"], top_comments["Comments"], color="lightgreen", edgecolor="black")
axes[2].set_title("En Fazla Yorum Yapılan Sanatçılar", fontsize=16)
axes[2].set_xlabel("Sanatçılar", fontsize=12)
axes[2].set_ylabel("Yorum Sayısı", fontsize=12)
axes[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
