# En dans edilebilir, enerjik ve akustik şarkılar analiz ediliyor
top_danceability = df.nlargest(10, 'Danceability')[['Artist', 'Danceability']]
print("En dans edilebilir şarkılar:")
print(top_danceability)

top_energy = df.nlargest(10, 'Energy')[['Artist', 'Energy']]
print("\nEn yüksek enerjiye sahip şarkılar:")
print(top_energy)

top_acousticness = df.nlargest(10, 'Acousticness')[['Artist', 'Acousticness']]
print("\nEn akustik şarkılar:")
print(top_acousticness)
