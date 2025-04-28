-- Tabloyu tanıyalım.

SELECT 
    column_name AS sutun_adi,      -- Sütun adını getirir ve 'sutun_adi' olarak etiketler
    data_type AS veri_tipi,           -- Sütunun veri tipini getirir ve 'veri_tipi' olarak etiketler
    character_maximum_length AS maksimum_uzunluk     -- Varchar gibi karakter veri tiplerinin maksimum uzunluğunu getirir
FROM 
    information_schema.columns -- Tabloların ve sütunların tanımlandığı sistem tablosu
WHERE 
    table_name = 'orders' -- 'orders' tablosuna ait sütunları filtreler
ORDER BY 
    ordinal_position; -- Sütunları tabloda tanımlandığı sıraya göre sıralar

	
	
	--Sipariş Ülkelerini ve Sipariş Sayısını Gösteren Sorgu

SELECT 
    ship_country AS ulke,      -- Siparişin gönderildiği ülkeyi getirir ve 'ulke' olarak etiketler
    COUNT(*) AS siparis_sayisi  -- Her ülke için toplam sipariş sayısını sayar ve 'siparis_sayisi' olarak etiketler
FROM 
    orders           -- 'orders' tablosundan veri çeker
GROUP BY 
    ship_country          -- Sonuçları ülke bazında gruplar
ORDER BY 
    siparis_sayisi DESC;     -- Sipariş sayısına göre azalan sırayla sıralar


    -- Kategori bazlı.
	-- Tablomuzu tanıyalım.
SELECT 
    column_name AS sutun_adi, -- 'column_name' sütununu seçiyoruz ve 'sutun_adi' olarak adlandırıyoruz.
    data_type AS veri_tipi, -- 'data_type' sütununu seçiyoruz ve 'veri_tipi' olarak adlandırıyoruz. Bu sütun, sütunun veri tipini belirtir .
    character_maximum_length AS maksimum_uzunluk -- 'character_maximum_length' sütununu seçiyoruz ve 'maksimum_uzunluk' olarak adlandırıyoruz. Bu, karakter veri tiplerinde maksimum uzunluğu ifade eder. Diğer veri tiplerinde NULL olabilir.
FROM 
    information_schema.columns -- 'information_schema.columns' sistem görünümünden sütun bilgilerini alıyoruz. Bu görünüm, bir tabloda bulunan tüm sütunların yapı bilgilerini içerir.
WHERE 
    table_name = 'categories' -- 'categories' adlı tabloya ait sütunları filtreliyoruz.
ORDER BY 
    ordinal_position; -- Sütunları tabloda göründükleri sıraya göre sıralıyoruz ('ordinal_position' sütununa göre).

	
	
	
	
	-------

--Kategorilere Göre Ürünlerin Toplam Geliri
SELECT 
    c.category_name, -- Her bir kategori için kategori adını seçiyoruz.
    TO_CHAR(SUM(od.quantity * od.unit_price), 'FM999G999G999') AS total_revenue 
    -- Sipariş detaylarından ürün miktarı ile birim fiyatını çarpıp toplam geliri hesaplıyoruz. 
    -- 'TO_CHAR' fonksiyonunu kullanarak sayıyı binlik ayırıcılarla (örn. 1,000,000) formatlıyoruz.
FROM 
    categories c -- 'categories' tablosundan başlıyoruz.
LEFT JOIN 
    products p ON c.category_id = p.category_id 
    -- 'categories' tablosunu 'products' tablosuyla birleştiriyoruz. 
    -- Bağlantı, 'category_id' üzerinden yapılıyor. Sol birleştirme, kategorilere ait olmayan ürünler için de satır döndürür.
LEFT JOIN 
    order_details od ON p.product_id = od.product_id 
    -- Daha sonra 'products' tablosunu 'order_details' tablosuyla birleştiriyoruz. 
    -- Bağlantı, 'product_id' üzerinden yapılıyor. Sol birleştirme, ürünlere ait olmayan sipariş detaylarını da tutar.
GROUP BY 
    c.category_name 
    -- Kategorilere göre gruplama yapıyoruz. Her kategori için bir satır döner.
ORDER BY 
    total_revenue DESC; 
    -- Hesaplanan toplam gelir değerine göre sıralama yapıyoruz. En yüksek gelir üstte olacak şekilde sıralanır.



----En çok sipariş edilen ürün kategorisini bulmak

SELECT 
    c.category_name AS kategori_adi, -- Kategorinin adını alır ve 'kategori_adi' olarak etiketler
    SUM(od.quantity) AS toplam_siparis -- Bu kategoride toplam sipariş edilen ürün miktarını hesaplar ve 'toplam_siparis' olarak etiketler
FROM 
    categories c -- Kategorileri içeren tablo
JOIN 
    products p ON c.category_id = p.category_id -- Kategorileri ürünlerle eşleştirir (category_id üzerinden)
JOIN 
    order_details od ON p.product_id = od.product_id -- Ürünleri sipariş detaylarıyla eşleştirir (product_id üzerinden)
GROUP BY 
    c.category_name -- Sonuçları kategori adına göre gruplar
ORDER BY 
    toplam_siparis DESC; -- Toplam sipariş miktarına göre azalan sırada sıralar

------senaryo sorguları.


-- Gelir Analizi (Toplam Satış Geliri ve Yıllık Dağılımı)
SELECT 
    EXTRACT(YEAR FROM o.order_date) AS yil, -- Sipariş tarihinden yılı çıkarıyoruz.
    TO_CHAR(SUM(od.quantity * od.unit_price), 'FM999G999G999D00') AS toplam_gelir -- Toplam geliri formatlıyoruz.
    -- 'FM999G999G999D00' ile binlik ayırıcı (G) ve iki ondalık (D00) ekliyoruz. 
FROM 
    orders o
JOIN 
    order_details od ON o.order_id = od.order_id -- Sipariş detaylarını siparişlerle birleştiriyoruz.
GROUP BY 
    EXTRACT(YEAR FROM o.order_date) -- Yıllara göre gruplama yapıyoruz.
ORDER BY 
    yil; -- Yıllara göre sıralıyoruz.


	-- Müşteri Analizi (En Çok Sipariş Veren Müşteriler)


SELECT 
    c.customer_id AS musteri_id, -- Müşteri kimliklerini seçiyoruz.
    c.company_name AS musteri_adi, -- Müşteri şirket isimlerini seçiyoruz.
    COUNT(o.order_id) AS toplam_siparis -- Her bir müşterinin verdiği toplam sipariş sayısını hesaplıyoruz.
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id -- Müşterileri siparişlerle birleştiriyoruz.
GROUP BY 
    c.customer_id, c.company_name -- Müşteri kimlik ve isimlerine göre gruplama yapıyoruz.
ORDER BY 
    toplam_siparis DESC -- Toplam sipariş sayısına göre azalan sıralama yapıyoruz.
LIMIT 10; -- En çok sipariş veren ilk 10 müşteriyi gösteriyoruz.


--Kargo Analizi (Kargo Şirketlerine Göre Taşınan Sipariş Sayısı ve Toplam Gelir)

SELECT 
    s.shipper_id AS kargo_id, -- Kargo şirketi kimliği.
    s.company_name AS kargo_adi, -- Kargo şirketinin adı.
    COUNT(o.order_id) AS toplam_siparis, -- Kargo edilen siparişlerin toplam sayısı.
    TO_CHAR(SUM(od.quantity * od.unit_price), 'FM999G999G999D00') AS toplam_gelir 
    -- Toplam geliri formatlıyoruz: 
    -- 'FM' boşlukları kaldırır, 'G' binlik ayırıcı ekler, 'D00' noktadan sonra iki basamak yuvarlar.
FROM 
    shippers s
JOIN 
    orders o ON s.shipper_id = o.ship_via -- Kargo şirketlerini siparişlerle birleştiriyoruz.
JOIN 
    order_details od ON o.order_id = od.order_id -- Sipariş detaylarını ekliyoruz.
GROUP BY 
    s.shipper_id, s.company_name -- Kargo şirketlerine göre gruplama yapıyoruz.
ORDER BY 
    toplam_gelir DESC; -- Toplam gelire göre azalan sırada sıralama yapıyoruz.



	--Kategori Geliri Analizi (Her Kategorinin Toplam Geliri ve Ürün Sayısı)


SELECT 
    c.category_name AS kategori_adi, -- Kategori adını seçiyoruz.
    COUNT(p.product_id) AS urun_sayisi, -- Her kategorideki ürün sayısını hesaplıyoruz.
    TO_CHAR(SUM(od.quantity * od.unit_price), 'FM999G999G999D00') AS toplam_gelir 
    -- Toplam geliri formatlıyoruz:
    -- 'FM': Fazladan boşlukları kaldırır.
    -- 'G': Binlik ayırıcı ekler.
    -- 'D00': Noktadan sonra iki ondalık basamak gösterir.
FROM 
    categories c
JOIN 
    products p ON c.category_id = p.category_id -- Kategorileri ürünlerle birleştiriyoruz.
JOIN 
    order_details od ON p.product_id = od.product_id -- Ürünleri sipariş detaylarıyla birleştiriyoruz.
GROUP BY 
    c.category_name -- Kategorilere göre gruplama yapıyoruz.
ORDER BY 
    toplam_gelir DESC; -- Toplam gelire göre sıralıyoruz.


-- RFM ANALIZI
-- Recency: En son sipariş tarihi ve '1998-05-06' tarihine göre geçen gün sayısını hesaplama
-- RFM ANALIZI
SELECT MAX(order_date) 
FROM orders; -- Siparişlerin en son tarihini kontrol ediyoruz.
-- '1998-05-06' tarihi analiz için referans alınıyor.

WITH recency AS (
    SELECT o.customer_id, -- Müşteri kimliği
           MAX(o.order_date) AS max_order_date, -- Müşteri için en son sipariş tarihi
           '1998-05-06'::date - MAX(o.order_date) AS days_since_last_order -- 1998-05-06'ya kadar geçen gün sayısı
    FROM orders o
    WHERE o.shipped_date IS NOT NULL -- Sevk edilmiş siparişleri filtreliyoruz.
    GROUP BY o.customer_id -- Her müşteri için gruplama yapıyoruz.
),
frequency AS (
    SELECT o.customer_id, -- Müşteri kimliği
           COUNT(o.order_id) AS order_frequency -- Müşterinin verdiği toplam sipariş sayısı
    FROM orders o
    WHERE o.shipped_date IS NOT NULL -- Sadece sevk edilmiş siparişleri alıyoruz.
    GROUP BY o.customer_id -- Her müşteri için gruplama yapıyoruz.
),
monetary AS (
    SELECT o.customer_id, -- Müşteri kimliği
           SUM(od.unit_price * od.quantity) AS monetary -- Müşterinin toplam harcaması (birim fiyat x miktar)
    FROM orders o
    JOIN order_details od ON o.order_id = od.order_id -- Siparişler ve sipariş detaylarını birleştiriyoruz.
    WHERE o.shipped_date IS NOT NULL -- Sadece sevk edilmiş siparişleri dahil ediyoruz.
    GROUP BY o.customer_id -- Her müşteri için gruplama yapıyoruz.
),
rfm_scores AS (
    SELECT 
        COALESCE(r.customer_id, f.customer_id, m.customer_id) AS customer_id, -- Her müşterinin kimliği.
        
        -- Recency skorlarının atanması (son sipariş tarihi)
        CASE
            WHEN r.days_since_last_order <= 30 THEN 5 -- Son 30 gün içinde sipariş verdiyse skor 5.
            WHEN r.days_since_last_order <= 60 THEN 4 -- Son 31-60 gün içinde sipariş verdiyse skor 4.
            WHEN r.days_since_last_order <= 90 THEN 3 -- Son 61-90 gün içinde sipariş verdiyse skor 3.
            WHEN r.days_since_last_order <= 120 THEN 2 -- Son 91-120 gün içinde sipariş verdiyse skor 2.
            ELSE 1 -- 120 günden uzun süre önce sipariş verdiyse skor 1.
        END AS recency_score, -- Recency skoru sütunu.

        -- Frequency skorlarının atanması (sipariş sıklığı)
        CASE
            WHEN f.order_frequency > 10 THEN 5 -- 10'dan fazla sipariş verdiyse skor 5.
            WHEN f.order_frequency > 5 THEN 4 -- 6-10 arası sipariş verdiyse skor 4.
            WHEN f.order_frequency >= 3 THEN 3 -- 3-5 arası sipariş verdiyse skor 3.
            WHEN f.order_frequency >= 1 THEN 2 -- 1-2 arası sipariş verdiyse skor 2.
            ELSE 1 -- Hiç sipariş vermediyse skor 1.
        END AS frequency_score, -- Frequency skoru sütunu.

        -- Monetary skorlarının atanması (toplam harcama)
        CASE
            WHEN m.monetary >= 1000 THEN 5 -- 1000 ve üstü harcadıysa skor 5.
            WHEN m.monetary >= 500 THEN 4 -- 500-999 arası harcadıysa skor 4.
            WHEN m.monetary >= 100 THEN 3 -- 100-499 arası harcadıysa skor 3.
            WHEN m.monetary >= 50 THEN 2 -- 50-99 arası harcadıysa skor 2.
            ELSE 1 -- 50'nin altında harcadıysa skor 1.
        END AS monetary_score -- Monetary skoru sütunu.

    FROM recency r
    FULL OUTER JOIN frequency f ON r.customer_id = f.customer_id
    FULL OUTER JOIN monetary m ON r.customer_id = m.customer_id
),
rfm_segments AS (
    SELECT 
        customer_id, -- Her müşterinin kimliği.
        recency_score, -- Recency skoru.
        frequency_score, -- Frequency skoru.
        monetary_score, -- Monetary skoru.
        (recency_score + frequency_score + monetary_score) AS total_score, -- Toplam skor (RFM'nin toplamı).

        -- Toplam skora göre segmentlerin atanması
        CASE
            WHEN (recency_score + frequency_score + monetary_score) >= 12 THEN 'VIP Customer' -- Toplam skor >= 12.
            WHEN (recency_score + frequency_score + monetary_score) >= 9 THEN 'Loyal Customer' -- Toplam skor 9-11 arası.
            WHEN (recency_score + frequency_score + monetary_score) >= 6 THEN 'New Customer' -- Toplam skor 6-8 arası.
            ELSE 'At Risk Customer' -- Toplam skor < 6.
        END AS segment -- Segment sütunu.
    FROM rfm_scores -- Daha önce hesaplanan RFM skorlarından segmentleri oluşturuyoruz.
)
SELECT *
FROM rfm_segments
ORDER BY total_score DESC; -- Toplam skora göre azalan sıralama.
