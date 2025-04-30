import matplotlib.pyplot as plt

fig, axes = plt.subplots(3, 1, figsize=(12, 18))

axes[0].bar(top_danceability["Artist"], top_danceability["Danceability"], color="skyblue", edgecolor="black")
axes[0].set_title("En Dans Edilebilir Şarkılar", fontsize=16)
axes[0].set_xlabel("Sanatçılar")
axes[0].set_ylabel("Dans Edilebilirlik")
axes[0].tick_params(axis='x', rotation=45)

axes[1].bar(top_energy["Artist"], top_energy["Energy"], color="salmon", edgecolor="black")
axes[1].set_title("En Yüksek Enerjiye Sahip Şarkılar", fontsize=16)
axes[1].set_xlabel("Sanatçılar")
axes[1].set_ylabel("Enerji")
axes[1].tick_params(axis='x', rotation=45)

axes[2].bar(top_acousticness["Artist"], top_acousticness["Acousticness"], color="lightgreen", edgecolor="black")
axes[2].set_title("En Akustik Şarkılar", fontsize=16)
axes[2].set_xlabel("Sanatçılar")
axes[2].set_ylabel("Akustiklik")
axes[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
