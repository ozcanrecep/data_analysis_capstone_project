import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# Veri: Müşteri bazlı toplam sipariş sayısı
# ----------------------------------------

# DataFrame verisi manuel olarak oluşturuluyor
data = {
    "musteri_id": ["SAVEA", "ERNSH", "QUICK", "FOLKO", "HUNGO"],
    "musteri_adi": [
        "Save-a-lot Markets",
        "Ernst Handel",
        "QUICK-Stop",
        "Folk och få HB",
        "Hungry Owl All-Night Grocers"
    ],
    "toplam_siparis": [31, 30, 28, 19, 19]
}
df = pd.DataFrame(data)  # Veriler pandas DataFrame'e dönüştürülüyor

# ----------------------------------------
# Grafik: Müşterilere göre toplam sipariş
# ----------------------------------------

plt.figure(figsize=(10, 6))  # Grafik boyutu ayarlanıyor

# Çubuk grafik çiziliyor
plt.bar(df['musteri_adi'], df['toplam_siparis'],
        color='salmon', edgecolor='black')

# Grafik başlığı ve eksen adları
plt.title("Müşterilere Göre Toplam Sipariş Sayısı", fontsize=14)
plt.xlabel("Müşteri Adı", fontsize=12)
plt.ylabel("Toplam Sipariş", fontsize=12)

# X ekseni etiketleri yataydan eğik hale getiriliyor (daha okunaklı)
plt.xticks(rotation=45, ha="right")

# Y eksenine ızgara çizgileri ekleniyor
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafik kenar boşlukları otomatik ayarlanıyor
plt.tight_layout()

# Grafik ekranda gösteriliyor
plt.show()
