import pandas as pd                # Veri işleme için pandas kütüphanesi
import matplotlib.pyplot as plt    # Grafik çizimi için matplotlib kütüphanesi

# ----------------------------------------
# Veri: Yıllara göre toplam gelir bilgisi
# ----------------------------------------

# Yıl ve toplam gelir verilerini içeren sözlük yapısı oluşturuluyor
data = {
    "yıl": [1996, 1997, 1998],
    "toplam_gelir": [226298.50, 658388.75, 469771.34]
}

# Veriler pandas DataFrame'e dönüştürülüyor
df = pd.DataFrame(data)

# ----------------------------------------
# Grafik Oluşturma
# ----------------------------------------

plt.figure(figsize=(10, 6))  # Grafik boyutu (genişlik, yükseklik) ayarlanıyor

# Çizgi grafiği çiziliyor
plt.plot(
    df['yıl'],                # X ekseni: yıllar
    df['toplam_gelir'],       # Y ekseni: gelir
    marker='o',               # Veri noktalarına daire işareti ekle
    linestyle='-',            # Düz çizgi kullan
    linewidth=2,              # Çizgi kalınlığı
    markersize=6,             # Nokta büyüklüğü
    color='b'                 # Mavi renk
)

# Y eksenine binlik ayırıcı (virgül) formatı uygulanıyor
plt.gca().get_yaxis().set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{x:,.0f}')
)

# Her veri noktasının üstüne değerleri yaz
for x, y in zip(df['yıl'], df['toplam_gelir']):
    plt.text(x, y, f"{y:,.0f}", ha='center', va='bottom', fontsize=10)

# Grafik başlığı ve eksen etiketleri
plt.title("Yıllara Göre Toplam Gelir", fontsize=14)  # Başlık
plt.xlabel("Yıl", fontsize=12)                       # X ekseni etiketi
plt.ylabel("Toplam Gelir (TL)", fontsize=12)         # Y ekseni etiketi

# Arka plana grid (ızgara) çizgileri ekleniyor
plt.grid(True, linestyle='--', alpha=0.7)

# X ekseni için özel yıl aralıkları kullanılıyor
plt.xticks(df['yıl'])

# Önemli veri noktalarına açıklama (annotate) ekleniyor

# 1997'deki büyük artış
plt.annotate(
    "Büyük artış",
    xy=(1997, 658388.75), xytext=(1996.5, 700000),
    arrowprops=dict(facecolor='green', arrowstyle="->"),
    fontsize=12
)

# 1998'deki düşüş
plt.annotate(
    "Düşüş",
    xy=(1998, 469771.34), xytext=(1997.5, 500000),
    arrowprops=dict(facecolor='red', arrowstyle="->"),
    fontsize=12
)

# Grafik düzenlemesi ve gösterimi
plt.tight_layout()  # Kenar boşluklarını otomatik ayarla
plt.show()          # Grafiği göster
