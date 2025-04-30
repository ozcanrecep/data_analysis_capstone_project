import pandas as pd

# Veri yükleniyor
df = pd.read_csv("Spotify_Youtube.csv")

# En çok görüntüleme alan videolar
top_views = df.nlargest(10, 'Views')[['Artist', 'Views']]
print("En çok görüntüleme alan videolar (Sanatçılar dahil):")
print(top_views)

# En çok beğeni alan videolar
top_likes = df.nlargest(10, 'Likes')[['Artist', 'Likes']]
print("\nEn çok beğeni alan videolar (Sanatçılar dahil):")
print(top_likes)

# En fazla yorum yapılan içerikler
top_comments = df.nlargest(10, 'Comments')[['Artist', 'Comments']]
print("\nEn fazla yorum yapılan videolar (Sanatçılar dahil):")
print(top_comments)
