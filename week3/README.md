İHA GÖRÜNTÜ İŞLEME ve NESNE TAKİBİ
OpenCV - Hafta 3 Uygulamaları
Hazırlayan: Melisa Kahraman

PROJE ÖZETİ
Bu çalışma, İHA sistemlerinde kullanılan temel ve orta seviye görüntü işleme algoritmalarını kapsamaktadır. Görüntü filtrelemeden başlayarak, gerçek zamanlı hedef takibi ve yön algoritmasına kadar 8 farklı aşama uygulanmıştır. Tüm çıktı görselleri /outputs klasöründe yer almaktadır.

BÖLÜM 1: Görüntü Filtreleme ve Gürültü Temizleme

Amaç: İHA gibi platformlarda kamera titremesi ve ışık değişimi nedeniyle oluşan gürültüyü temizleyerek, kenar tespiti ve nesne tanıma adımlarının doğruluğunu artırmak.

Uygulanan Yöntemler:

Gaussian Blur: Görüntüyü genel olarak yumuşatır, sensör gürültüsünü azaltır. Hızlı sonuç istendiğinde ve gürültü az olduğunda tercih edilir.

Median Blur: Noktasal (tuz-biber) gürültüleri temizlemede en başarılı yöntemdir. Görüntüde karıncalanma çoksa ve piksel bozulmaları varsa kullanılır.

Bilateral Filter: Gürültüyü temizlerken nesne kenarlarını keskin tutar, detayları korur. Kenar bilgisinin ve nesne sınırlarının kritik olduğu İHA sistemlerinde, detay kaybını önlediği için en iyi tercihtir.



BÖLÜM 2: Görüntü Üzerine Çizim ve Yazı Ekleme

Amaç: Tespit edilen hedeflerin sınırlarını ve bilgilerini görselleştirerek raporlanabilir hale getirmek.

Yapılan İşlemler:

Çizimler: Farklı renk ve kalınlıklarda dikdörtgen, daire, poligon ve çizgi kullanılarak hedef işaretlemesi yapıldı.

İşaretleme: Nesnenin dış çerçevesi ve merkez noktası net bir şekilde belirtildi.

Metin: Görüntüye Türkçe karaktersiz, boyutu ve rengi ayarlanmış "HEDEF" ve "BOYUT" bilgileri eklendi.


BÖLÜM 3: Eşikleme ve Kenar Tespiti

Amaç: Görüntüdeki nesne sınırlarını bulmak ve analiz için görüntüyü siyah-beyaz (binary) formata indirgemek.

Eşikleme Yöntemleri ve Senaryolar:

Binary: Sabit ışıklı, basit sahnelerde hızlı sonuç için kullanılır.

Otsu: Işık seviyesinin otomatik belirlenmesi gereken, nesne ve arka planın kontrastı yüksek sahnelerde tercih edilir.

Adaptive: Işığın homojen dağılmadığı, gölgeli veya parlama olan sahnelerde her bölgeyi ayrı değerlendirdiği için en iyi sonucu verir.

Kenar Tespiti ve Filtre Etkisi:

Canny: Alt ve üst eşik değerleri artırıldığında sadece en güçlü kenarlar kalırken, değerler düşürüldüğünde daha fazla detay ve gürültü ortaya çıkar.

Ham vs Filtreli Karşılaştırma: Ham görüntüde Canny uygulandığında gürültüler de kenar gibi algılanıp görüntü kirliliği yaratırken; filtre uygulanmış görüntüde sadece nesne sınırları net ve temiz şekilde ortaya çıkmıştır.


BÖLÜM 4: Morfolojik İşlemler

Amaç: Eşikleme sonrası oluşan gürültüleri temizlemek, nesne sınırlarındaki kopuklukları gidermek ve kontur analizi öncesi görüntüyü iyileştirmek.

İşlemler ve Kullanım Senaryoları:

Erosion (Aşındırma): Nesne sınırlarını inceltir. Küçük beyaz gürültüleri yok etmek için kullanılır.

Dilation (Genişletme): Nesne sınırlarını kalınlaştırır. Nesne üzerindeki küçük siyah boşlukları veya kopuk çizgileri birleştirmek için kullanılır.

Opening (Açma): Önce aşındırma sonra genişletme yapar. Nesne dışındaki küçük gürültü piksellerini silmekte en başarılı yöntemdir.

Closing (Kapama): Önce genişletme sonra aşındırma yapar. Nesne içerisindeki delikleri kapatmak ve parçalı nesneleri bütünleştirmek için kullanılır.

Kernel (Çekirdek) Boyutu Etkisi:

Kernel boyutu büyüdükçe işlemin şiddeti artar. Çok büyük kernel, gürültüyle birlikte ana nesnenin de detaylarını kaybetmesine (aşırı aşınma veya aşırı şişme) neden olur.

Renk Maskesi ve Temizlik:

Renk maskesi üzerinde uygulanan morfolojik işlemler, maskede oluşan karıncalanma gürültülerini temizleyerek, nesnenin sadece ana gövdesinin kontur analizine girmesini sağlar.


BÖLÜM 5: Kontur Analizi

Amaç: Nesnelerin sınırlarını koordinat bazlı belirlemek; alan, çevre ve şekil analizi yaparak hedefleri sınıflandırmak.

Yapılan Analizler:

Alan Filtrelemesi: cv2.contourArea ile küçük konturlar elendi. Eşik değeri olarak 500 piksel seçildi; çünkü bu değerin altındaki yapılar İHA sistemleri için hedef değil, görüntü gürültüsü kabul edilir.

Hesaplamalar: Her kontur için Bounding Box oluşturuldu. Nesnenin alanı ve çevresi hesaplanarak görüntü üzerine dinamik olarak yazdırıldı.

Renklendirme: Tespit edilen en büyük 3 kontur, önem sırasına göre farklı renklerle (Kırmızı, Mavi, Sarı) işaretlenerek hiyerarşi sağlandı.

Şekil Tespiti (Karar Mekanizması):

approxPolyDP ile köşe sayıları analiz edildi.

Köşe sayısı 3 ise Üçgen, 4 ise Kare/Dikdörtgen, 10'dan fazla ise Daire/Elips olarak sınıflandırma yapıldı.


BÖLÜM 6: HSV ile Renk Bazlı Nesne Tespiti

Amaç: Belirli renkteki hedefleri ışık koşullarından etkilenmeden tespit etmek ve merkez koordinatlarını belirlemek.

Yapılan İşlemler:

Renk Uzayı Dönüşümü: Görüntü BGR'den HSV renk uzayına çevrildi. Bu sayede ışık şiddetindeki değişimlerden bağımsız olarak sadece renk tonu üzerinden maskeleme yapıldı.

Maskeleme ve Temizlik: Hedef renkler (Mavi ve Sarı) için inRange ile alt-üst sınırlar belirlendi. Oluşan maskelerdeki gürültüler morfolojik işlemlerle temizlendi.

Analiz ve Takip: Temizlenen maskelerden konturlar çıkarıldı. Moment hesaplaması ile nesnelerin kütle merkezleri (cx, cy) bulunarak görüntüye yazdırıldı.

Çoklu Nesne Tespiti:

Uygulama, aynı anda hem mavi hem de sarı nesneleri tespit edebilmektedir.

Ekranda her renk grubu için ayrı ayrı nesne sayısı dinamik olarak takip edilmektedir.


BÖLÜM 7: Template Matching (Şablon Eşleme)

Amaç: Elde bulunan sabit bir hedef görselini, büyük bir görüntü içerisinde piksel bazlı benzerlik taraması yaparak tespit etmek.

Yapılan İşlemler:

Şablon Oluşturma: Orijinal görüntüden küçük bir bölge (bir pencere detayı) kesilerek template.jpg olarak ayrıldı.

Eşleme Algoritması: cv2.matchTemplate fonksiyonu kullanılarak görüntü üzerinde tarama yapıldı. cv2.minMaxLoc ile en yüksek benzerlik puanına sahip koordinatlar belirlendi ve dikdörtgen içine alındı.

Çoklu Tespit: Belirlenen bir eşik değerinin üzerindeki tüm benzerlik puanları taranarak, görüntüdeki tüm benzer hedefler aynı anda işaretlendi.

Sınırlar ve YOLO ile Karşılaştırma:

Neden Yetersiz Kalır?: Template matching; nesnenin boyutu değiştiğinde, nesne döndüğünde veya ışık açısı farklılaştığında başarısız olur. Sadece şablonun birebir kopyasını arar.

YOLO Farkı: YOLO gibi derin öğrenme modelleri, nesneyi özellikleri üzerinden (kenar, doku, form) tanıdığı için farklı açılardan ve boyutlardan gelen hedefleri başarıyla tespit edebilir. Template matching sadece sabit ve değişmeyen şekiller için kullanışlıdır.


BÖLÜM 8: Gerçek Zamanlı Video İşleme ve Hedef Takibi

Amaç: Statik görüntülerde yapılan işlemleri canlı video akışına (Webcam) entegre etmek ve nesnenin konumuna göre yön bilgisi (Sağ, Sol, Orta) üreterek gerçek bir İHA otopilot sisteminin temel mantığını simüle etmek.

Yapılan İşlemler:

Canlı Takip: Webcam üzerinden alınan her karede belirlenen hedef renk (HSV) maskelenmiş, konturlar bulunarak nesne gerçek zamanlı olarak işaretlenmiştir.

Yön Mantığı: Ekran yatay eksende üç bölgeye ayrılmıştır. Nesne merkezinin koordinatına göre ekrana dinamik olarak "SOL", "ORTA" veya "SAG" bilgisi yazdırılmaktadır.

Canlı Veri: Ekranın köşesinde anlık FPS değeri ve o an görüntüde tespit edilen nesne sayısı kullanıcıya sunulmaktadır.

FPS Optimizasyonu ve Gözlemler:

Sorun: Başlangıçta yüksek çözünürlüklü kareler üzerinde işlem yapmak FPS değerini düşürmekteydi.

Uygulanan Optimizasyon: Görüntü işleme adımına girmeden önce cv2.resize kullanılarak kare boyutları küçültülmüştür. Bu sayede işlemci yükü azaltılmış ve FPS değeri yaklaşık %30-40 oranında artarak daha akıcı bir takip sağlanmıştır.

Neden Önemli?: Nesnenin merkez noktasının hangi bölgede olduğunun tespiti, otonom bir İHA'ya "Sağa Dön" veya "Sola Dön" komutunu verecek olan ana algoritmadır.

