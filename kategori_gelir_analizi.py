import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# Veri: Kategorilere göre ürün sayısı ve gelir
# ----------------------------------------

data = {
    "kategori_adi": ["Beverages", "Dairy Products", "Meat/Poultry", "Confections", "Seafood"],
    "urun_sayisi": [404, 366, 173, 334, 330],
    "toplam_gelir": ["286,526.95", "251,330.50", "178,188.80", "177,099.10", "141,623.09"]
}
df = pd.DataFrame(data)

# String formatındaki gelirleri float'a dönüştür
df['toplam_gelir'] = df['toplam_gelir'].str.replace(',', '').astype(float)

# ----------------------------------------
# Grafik: Kategorilere göre toplam gelir
# ----------------------------------------

plt.figure(figsize=(10, 6))
plt.bar(df['kategori_adi'], df['toplam_gelir'], color='skyblue', edgecolor='black')

# Y eksenine binlik ayırıcı formatı
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))

# Çubukların üstüne gelir değerlerini yaz
for i, val in enumerate(df['toplam_gelir']):
    plt.text(i, val, f"{val:,.0f}", ha='center', va='bottom', fontsize=10)

# Başlık ve eksenler
plt.title("Kategorilere Göre Toplam Gelir", fontsize=14)
plt.xlabel("Kategori Adı", fontsize=12)
plt.ylabel("Toplam Gelir (TL)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ----------------------------------------
# Açıklamalar: Veri üzerinden yorum
# ----------------------------------------

print("""
En Yüksek Gelir Getiren Kategori:
Beverages (İçecekler) kategorisi, 286,527 TL ile en yüksek gelir sağlayan kategoridir.

En Düşük Gelir Getiren Kategori:
Seafood (Deniz Ürünleri) kategorisi, 141,623 TL ile en düşük gelir sağlayan kategoridir.

İkinci En Yüksek Gelir Getiren Kategori:
Dairy Products (Süt Ürünleri) kategorisi, 251,330 TL ile ikinci sırada yer alır.

Benzer Gelir Getiren Kategoriler:
Meat/Poultry ve Confections kategorilerinin toplam gelirleri birbirine oldukça yakındır.

Genel Trend:
İçecekler ve süt ürünleri, toplam gelir açısından diğer kategorilere kıyasla belirgin fark yaratmaktadır.
""")
