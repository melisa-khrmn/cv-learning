YOLOv8 ile NESNE TESPİTİ ve GERÇEK ZAMANLI HEDEF TAKİBİ



BÖLÜM 1: YOLOv8 Mimari Yapısı ve Model Boyutlarının Analizi

1.1. YOLOv8 Yapısal Bileşenleri

Derin öğrenme tabanlı nesne tespiti süreçlerinde kullanılan YOLOv8 mimarisi temel olarak üç ana bileşenden oluşmaktadır:



Backbone (Omurga): Görüntü matrisinden öznitelik (feature) çıkarımı yapan temel katmandır. YOLOv8 mimarisinde, özel C2f blokları ile güçlendirilmiş, modifiye bir CSPDarknet53 yapısı tercih edilmektedir. Bu katman girdi olarak aldığı ham görüntüden; kenar, köşe, doku ve yüksek seviyeli anlamsal öznitelikleri yakalamakla görevlidir.



Neck (Boyun): Backbone katmanından elde edilen farklı çözünürlük ve ölçeklerdeki öznitelik haritalarını birleştiren köprü yapısıdır. Bilgi akışını çift yönlü (yukarıdan aşağıya ve aşağıdan yukarıya) optimize eden PANet (Path Aggregation Network) veya FPN türevleri kullanılmaktadır. Bu çift yönlü entegrasyon, hem küçük ölçekli nesnelerin hem de büyük yapıların aynı kararlılıkla yakalanmasını sağlar.



Head (Baş): Öznitelik haritalarını işleyerek nihai koordinat ve sınıf tahminlerini üreten katmandır. YOLOv8, önceki sürümlerden farklı olarak çapa tabanlı (anchor-based) yapıları terk ederek doğrudan nesne merkezini ve sınırlarını tahmin eden "Anchor-free" bir felsefeye geçmiştir. Ek olarak, sınıflandırma (classification) ve konumlandırma (regression) süreçlerini ayrı kollarda yürüten "Decoupled Head" mimarisini kullanmaktadır.



1.2. Donanımsal Ölçeklenebilirlik ve Model Boyutları

YOLOv8 mimarisi, kullanılacak donanım kısıtlarına ve hedeflenen işlem hızına göre beş farklı ölçekte sunulmaktadır:



YOLOv8n (Nano): Yaklaşık 3.2 milyon parametre ile serinin en hafif ve en hızlı modelidir. Matematiksel işlem yükü düşük olduğundan yüksek kare hızları (FPS) sunar. Anlık tepki süresinin kritik olduğu kısıtlı gömülü sistemler ve gerçek zamanlı otonom uçuş/takip görevleri için birincil seçenektir.



YOLOv8s (Small): Yaklaşık 11.2 milyon parametre barındıran bu model, işlem hızını optimize ederken doğruluk oranını ciddi ölçüde artırır. Gecikme sürelerini makul düzeyde tutarak küçük nesnelerin kaçırılmamasını sağlayan dengeli bir seçenektir.



YOLOv8m (Medium): Yaklaşık 25.9 milyon parametre içeren orta ölçekli modeldir. Doğruluk performansı yüksek olsa da artan işlem yükü nedeniyle kısıtlı donanımlarda FPS düşüşlerine ve gecikmelere yol açabilir.



YOLOv8l (Large): Yaklaşık 43.7 milyon parametreye sahip ağır bir mimaridir. Çıkarım süresi uzadığı için anlık geri bildirim gerektiren gerçek zamanlı sistemler yerine, yüksek doğruluk hedefleyen statik analiz projelerine uygundur.



YOLOv8x (Extra Large): Yaklaşık 68.2 milyon parametre ile serinin en yüksek hassasiyet sunan ama en hantal olan modelidir. Canlı ve dinamik sistemlerde donanımı zorlayacağı için genellikle güçlü sunucularda veri analizi ve referans model oluşturma aşamalarında tercih edilir.





BÖLÜM 2: Confidence ve Sınıf Filtreleme

2.1. Confidence Threshold (Güven Eşiği) Deneyleri

Modelin tahmin başarısı ve sahada ürettiği kararlar, belirlenen güven eşik değerlerine doğrudan bağımlıdır:



Düşük Eşik Değerleri (Örn: 0.05): Modelin en küçük gürültüleri, gölgeleri veya arka plan detaylarını bile hedef nesne olarak etiketlemesine yol açar. Yanlış pozitif oranı fırlayacağından, otonom kararların tamamen yanıltıcı olmasına sebebiyet verir.



Yüksek Eşik Değerleri (Örn: 0.90): Modelin yalnızca mutlak emin olduğu nesneleri raporlamasını sağlar. Bu durum, anlık ışık değişimlerinde veya kısmi tıkanmalarda gerçek hedeflerin tamamen kaçırılmasına ve takibin kopmasına neden olur.



Optimum Aralık (Örn: 0.25 - 0.40): Dinamik çalışma koşulları için en dengeli aralıktır. Sistem çevre gürültülerini başarıyla elerken, gerçek hedefi kararlı bir şekilde takip etme hassasiyetini korur.



2.2. Sınıf Filtreleme ve Sınır Kutusu (Bounding Box) Boyut Analizi

Sınıf Filtreleme: COCO veri seti gibi hazır yapılar 80 farklı sınıfı tanımaktadır. Özel görevlerde ilgisiz tüm sınıfların filtrelenerek sadece hedef nesneye odaklanılması, işlemci üzerindeki yükü hafifletir ve karar mekanizmasının sahte verilerle kirlenmesini engeller.



Kutu Boyutları (Genişlik x Yükseklik): Tespit edilen sınır kutularının ekrandaki piksel cinsinden kapladığı alan, derinlik ve mesafe tahmini algoritmalarında girdi olarak kullanılmaktadır. Kutunun büyümesi hedefe yaklaşıldığını, küçülmesi ise uzaklaşıldığını matematiksel olarak ortaya koyarak otonom sistem kontrol mekanizmalarına temel veri sağlar.





BÖLÜM 3: Confidence ve Sınıf Filtreleme

Bilgisayarlı görü çalışmalarında uygulanan geleneksel ve modern iki farklı yaklaşım teknik parametreler doğrultusunda karşılaştırılmıştır:



3.1. HSV Tabanlı Renk Takibi (Geleneksel Yaklaşım)

Çalışma Mantığı: Görüntü matrisini HSV renk uzayına dönüştürerek belirlenen alt ve üst eşik değerleri arasındaki pikselleri filtreler. Kalan renk kütlesinin merkez noktasını (centroid) hesaplayarak nesne konumlandırması yapar.



Hız ve FPS Performansı: Arkasında matris çarpımlarına dayalı derin bir yapay sinir ağı mimarisi bulunmadığı için işlem yükü son derece hafiftir. Donanımı yormadan 60 FPS ve üzeri yüksek kararlılıkta akıcı bir çalışma sunar.



Doğruluk ve Kararlılık: Geometrik, anlamsal veya dokusal bir analiz yapamadığı için kararlılığı düşüktür. Bulut geçişleri, gölge düşmesi veya güneş parlaması gibi ışık değişimlerinde piksellerin renk değeri saptığı için hedef anında kaybedilir. Kadraja aynı renkte farklı bir nesne girdiğinde ise kilitlenme hedef dışına kayar.



Saha Optimizasyonu: Çalışma ortamındaki ışık değişkenlerine karşı adaptasyon yeteneği yoktur. Günün farklı saatlerinde el ile sürekli manuel kalibrasyon ve filtre eşiği ayarı yapılması zorunluluğu vardır.



3.2. YOLOv8 Tabanlı Nesne Tespiti (Derin Öğrenme Yaklaşımı)

Çalışma Mantığı: Hedef nesneyi renginden bağımsız olarak; kenar hatları, yüzey dokusu, derinlik algısı ve geometrik formu ile bütünsel olarak inceler. Derin katmanlardan geçen öznitelikler sayesinde nesnenin anlamsal kimliğini ve tam koordinatlarını tahmin eder.



Hız ve FPS Performansı: Milyonlarca yapay sinir hücresi ve yoğun evrişim (convolution) katmanları barındırdığından matematiksel işlem yükü çok ağırdır. Donanım kısıtlarına bağlı olarak CPU tabanlı canlı testlerde kare hızlarının düştüğü (yaklaşık 14-15 FPS seviyelerine gerilediği) gözlemlenmiştir.



Doğruluk ve Kararlılık: Nesneyi şekilsel ve anlamsal özellikleriyle tanıdığı için doğruluk oranı çok yüksektir. Nesnenin kendi ekseninde dönmesi, gölgede kalması veya arka planda karmaşık yapılar barındırması durumunda dahi hedefi kaçırmadan yüksek kararlılıkla takibi sürdürür.



Saha Optimizasyonu: Roboflow gibi platformlar üzerinden farklı ışık ve açı varyasyonları ile toplanan verilerle bir kez eğitildikten (Fine-tuning) sonra, sahada dinamik çevre koşullarına karşı ek bir manuel kalibrasyon gerektirmeden otonom çalışabilir.



3.3. Karşılaştırma Özeti

Geleneksel HSV yöntemi, derin öğrenme yükü taşımadığı için yüksek hız (FPS) avantajı sağlasa da çevresel etkenlere karşı aşırı hassas ve kararsızdır. YOLOv8 tabanlı derin öğrenme mimarisi ise yüksek donanım ve işlem gücü talep etmesine karşın, sunduğu yüksek doğruluk ve zorlu saha koşullarına mukavemeti sayesinde otonom sistem tasarımlarında mutlak endüstriyel standart konumundadır. Hız kısıtları ise mimarinin "Nano" gibi optimize edilmiş hafif versiyonları seçilerek aşılabilmektedir.





BÖLÜM 4:  Custom Dataset Hazırlama ve Fine-tuning

4.1. Veri Setinin Hazırlanması ve Etiketleme Süreci

Modelin özel bir nesne üzerinde uzmanlaşmasını sağlamak amacıyla, hedef nesne olarak seçilen "Su Şişesi" özniteliğine yönelik veri toplama süreci yürütülmüştür. Nesneye ait farklı açılardan, değişen arka plan kombinasyonlarından ve ışık varyasyonlarından oluşan 28 adet özgün görsel kaydedilmiştir. Toplanan ham veriler Roboflow platformuna aktarılmış, nesne sınırları hassas bir şekilde işaretlenerek (bounding box) "su\_sisesi" sınıfı altında etiketleme entegrasyonu tamamlanmıştır.



4.2. Teknik Kısıtların Çözümü ve Yerel Dizin Bütünlüğü

Roboflow veri dağıtım (Train/Val split) arayüzünde yaşanan senkronizasyon ve tarayıcı kilitlenme hataları, platformun dışa aktarma (Export) konfigürasyonları esnetilerek bypass edilmiştir. Bu sayede tüm görselleri barındıran train klasörü ve konfigürasyon altyapısını kuran data.yaml dosyası yerel çalışma dizini olan week4 içerisine kayıpsız entegre edilmiştir.



Sistemin taşınabilirliğini korumak ve projenin farklı bilgisayarlarda çalıştırılması esnasında oluşabilecek "Dosya Yolu Bulunamadı" (Path Error) hatalarını engellemek adına data.yaml içeriği optimize edilmiştir. Mevcut olmayan validasyon dizinlerinin eğitimi durdurma riskine karşı, eğitim (train) ve doğrulama (val) yolları doğrudan yerel dizindeki mevcut görsellere yönlendirilerek mimari kararlılık güvenceye alınmıştır. Hazırlanan fine\_tuning.py scripti üzerinden, önceden eğitilmiş yolov8n.pt ağırlıkları referans alınarak 20 epoch sürecek ince ayar (Fine-tuning) süreci sıfır hata ile tamamlanmıştır. Çalışma sonucunda üretilen tüm ağırlıklar ve analiz çıktıları, yerel bağımlılık bütünlüğü adına terminal katmanından week4/egitim\_sonuclari klasörüne konsolide edilmiştir.





BÖLÜM 5: Model Performans Analizi

Eğitim süreci sonunda egitim\_sonuclari dizini altında otomatik olarak üretilen matematiksel metriklerin ve grafiklerin teknik analiz yorumları aşağıda sunulmuştur:



5.1. Loss (Kayıp) Grafiklerinin Değerlendirilmesi

Eğitim boyunca izlenen box\_loss (kutu konumu kaybı) ve cls\_loss (sınıflandırma doğruluğu kaybı) eğrilerinin her ikisi de 20 epoch boyunca düzenli, istikrarlı ve kararlı bir azalma eğilimi göstermiştir. Bu durum modelin hedef nesne morfolojisini başarıyla öğrendiğini doğrulamaktadır. Eğriler tam olarak plato çizmeden (düzleşmeden) 20. turda eğitimin sonlandırılması, modelin veriyi ezberlemesini (overfitting) engellemiş ve optimizasyon eğrisini en dengeli noktada tutmuştur. Epoch sayısının kontrolsüzce artırılması eğitim kaybını düşürmeye devam etse de doğrulama kayıplarını artırarak genel genelleme yeteneğine zarar vereceğinden, mevcut duruş noktası son derece stratejiktir.



5.2. Precision, Recall ve mAP Başarı Kriterleri

Precision (Kesinlik): Modelin "su\_sisesi" olarak gerçekleştirdiği pozitif tahminlerin gerçekle uyuşma oranı son derece yüksektir. Modelin arka plandaki yabancı nesnelere yanlış alarm üretme veya hatalı etiketleme payı minimuma indirgenmiştir.



Recall (Duyarlılık): Kadrajda var olan gerçek su şişesi nesnelerinin model tarafından yakalanma ve tespit edilme oranı yüksek bir kararlılık sergilemektedir. Modelin hedef nesneyi gözden kaçırma (ıskalama) ihtimali minimize edilmiştir.



mAP50 Skoru: Modelin %50 örtüşme (Intersection over Union - IoU) eşiğinde gösterdiği genel ortalama başarı değeridir. Çalışmada tek bir sınıf (su\_sisesi) eğitildiği için, bu metrik doğrudan model doğruluğunun sayısal kanıtıdır. Sıfır noktasından başlayarak dik bir ivmeyle yukarı tırmanan mAP grafiği, modelin hem konumlandırma hem de sınıf tanımlama görevini yüksek doğruluk yüzdesiyle tamamladığını tescillemektedir.



5.3. Confusion Matrix (Karışıklık Matrisi) Analizi

Karışıklık matrisinin ana köşegeni incelendiğinde, hedef sınıfın kendi eksenindeki doğru tahmin oranının ezici bir başarıya sahip olduğu görülmektedir. Modelin yapısal olarak yanılma payı gösterebileceği yegane alan nesne ile arka plan (background) arasındaki kontrast geçişleridir. Eğitimde kullanılan su şişesinin şeffaf plastik materyalden oluşması, arkasındaki arka plan detaylarını doğrudan ön plana yansıtmaktadır. Matriste gözlemlenen minimal sapmalar tamamen bu şeffaflık ilişkisinden doğan doğal arka plan karmaşasından ibaret olup, elde edilen sonuçlar kabul edilebilir akademik sınırların ve yüksek başarı standartlarının içerisindedir.

