import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# Veri: Kargo firmalarına göre toplam sipariş ve gelir
# ----------------------------------------

# Kargo ID, adı, sipariş sayısı ve gelir bilgileri manuel olarak giriliyor
data = {
    "kargo_id": [2, 3, 1],
    "kargo_adi": ["United Package", "Federal Shipping", "Speedy Express"],
    "toplam_siparis": [864, 645, 646],
    "toplam_gelir": [572724.58, 407750.82, 373983.19]
}

# Veriler pandas DataFrame'e aktarılıyor
df = pd.DataFrame(data)

# ----------------------------------------
# Grafik: Kargo şirketlerine göre toplam gelir
# ----------------------------------------

plt.figure(figsize=(10, 6))  # Grafik boyutu ayarlanıyor

# Çubuk grafik çiziliyor
plt.bar(df['kargo_adi'], df['toplam_gelir'],
        color='skyblue', edgecolor='black')

# Grafik başlığı ve eksen etiketleri
plt.title("Kargoların Toplam Gelirleri", fontsize=14)
plt.xlabel("Kargo Adı", fontsize=12)
plt.ylabel("Toplam Gelir (TL)", fontsize=12)

# X ekseni etiketlerini eğik hale getiriyoruz (okunabilirlik için)
plt.xticks(rotation=45)

# Y eksenine grid çizgileri ekleniyor
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Kenar boşlukları otomatik ayarlanıyor
plt.tight_layout()

# Grafik gösteriliyor
plt.show()
