# FIRAT ÜNİVESİTESİ
# GÖRÜNTÜ İŞLEME EKOSİSTEMİNE GİRİŞ

**Hazırlayan :** Melisa Kahraman
**Tarih :** 26.04.2026

## Bu Alanın Amacı
Görüntü işlemenin amacı, dijital görüntüleri analiz ederek anlamlı veriler çıkarmaktır. Bilgisayarların verileri insan gözüyle algılamasını ve yorumlamasını sağlayan bu teknoloji, bilgiyi daha anlaşılır bir formata dönüştürür. OpenCV, ham görsel veriyi matematiksel matrislere çevirerek nesne tespiti, yüz tanıma ve hareket analizi gibi karmaşık işlemleri gerçek zamanlı olarak gerçekleştirmemizi sağlar. Özellikle otonom sistemlerde ve İHA teknolojilerinde çevresel verilerin hızla işlenip kritik kararlar alınmasında büyük önem taşımaktadır.

## Temel Kavramlar
* **OpenCV (Open Source Computer Vision Library - Açık Kaynaklı Bilgisayarlı Görüntüleme) :** Görüntü işleme ve makine öğrenmesi için geliştirilmiş, en yaygın kullanılan açık kaynaklı kütüphanlerdendir.
* **Pixel :** Dijital görüntüyü oluşturan, kontol edilebilir, renk ve koordinat bilgisi taşıyan en küçük birimdir.
* **ROİ (Region of İnterest – İlgi Bölgesi) :** Görüntünün tamamı yerine üzerinde işlem yapılacak belirli bir alanı ifade eder.
* **FPS (Frames Per Second – Saniye Başına Kare Sayısı) :** Videolar sırasında bir saniyede ekrana yansıyan ardışık görüntü sayısıdır.
* **Gürültü (Noise) :** Görüntü üzerindeki istenmeyen sesler, lekeler ve karmaşıklıklardır.
* **Kenar Algılama (Edge Detection) :** Nesnelerin sınırlarını belirlemek için piksel değerlerindeki ani değişimleri tespit eden tekniktir.
* **Eşikleme (Thresholding) :** Görüntüyü belirli bir değerin altındakiler ve üstündekiler olarak ayırarak nesne belirginleştirme işlemidir.
* **Morfolojik İşlemler :** Görüntüdeki küçük gürültüleri temizlemek veya nesne yapılarını genişletip daraltmak için kullanılan matematiksel işlemlerdir.
* **Bounding Box (Sınırlayıcı Kutu) :** Görüntü üzerinde tespit edilen nesneyi içine alan dikdörtgen bir çerçevedir.
* **Telemetri :** İHA'nın hızı, irtifası, konumu gibi kritik verilerin anlık olarak yer istasyonuna iletilmesidir.

## Görüntü İşleme Pipeline'ı

  <img width="731" height="220" alt="Başlıksız Diyagram drawio (3)" src="https://github.com/user-attachments/assets/4c6fe292-3975-4919-b86e-75bac093662d" />


## Renk Uzayları

| Renk Uzayı | Açılımı / Anlamı | Kullanım Alanı | Tercih Nedeni |
| :--- | :--- | :--- | :--- |
| **RGB** | Red, Green, Blue | Dijital Ekranlar ve genel görüntüleme formatıdır. | Standart ekran görüntüleme formatıdır. |
| **BGR** | Blue, Green, Red | OpenCV kütüphanesinin varsayılan okuma formatıdır. | OpenCV'nin varsayılan okuma formatıdır. |
| **HSV** | Hue, Saturation, Value | Renk tespiti ve maskeleme; ışıktan az etkilenir. | Işık değişimlerinden az etkilenir, renkleri ayırmak kolaydır. |

## YOLO Versiyonları Karşılaştırması

| Model | Öne Çıkan Özellik | Kullanım Amacı | Donanım İhtiyacı |
| :--- | :--- | :--- | :--- |
| **YOLOv5** | Stabilite ve yaygın dokümantasyon desteği. | Standart nesne tespiti projeleri. | Düşük / Orta donanımlarda stabil çalışma. |
| **YOLOv8** | Çok yönlü mimari (Segmentasyon ve Takip). | Gelişmiş otonom sistemler. | Orta seviye GPU gereksinimi. |
| **YOLOv11** | Maksimum FPS ve verimlilik artışı. | Gerçek zamanlı İHA sistemleri. | Düşük kaynak tüketimi ile yüksek verimlilik. |

## GitHub Repoları Değerlendirmesi

| Repo | Yazılım Dili | Öne Çıkan Özellik | Yıldız Sayısı |
| :--- | :--- | :--- | :--- |
| opencv/opencv | C++ / Python | Temel görüntü işleme kütüphanesi. | 78.500+ |
| ultralytics/ultralytics | Python | YOLOv8 ve YOLOv11 resmi merkezi. | 32.200+ |
| sezer-muhammed/Eflatun-IHA | Python | Savaşan İHA kilitlenme kodları. | 100+ |

## Bu Hafta Öğrendiğim 3 Şey
1. Bir görüntünün kameradan alınıp otonom bir karara dönüşene kadar geçtiği işlem basamaklarını analiz ettim. Ham verinin ön işleme, öznitelik çıkarımı ve nesne tespiti gibi aşamalardan oluşan bir bütün olduğunu keşfettim.
2. Görüntü işlemede ışık değişimlerinin nesne tespitini ne kadar zorlaştırdığını gördüm. Standart RGB formatı yerine renkleri ışık şiddetinden ayıran HSV renk uzayını kullanmanın, dış ortamlarda çalışan İHA sistemleri için neden hayati bir gereklilik olduğunu öğrendim.
3. Karmaşık görünen otonom sistemlerin ve profesyonel projelerin aslında ulaşılmaz olmadığını, dünya standartlarındaki kodların GitHub üzerinde ne kadar şeffaf bir şekilde paylaşıldığını gördüm. Sektör lideri kütüphanelerin ve başarılı yerli projelerin kod yapılarını inceleyerek, küresel bilgi birikimine erişimin önemini kavradım.

## Kafama Takılan Sorular
* YOLOv11 gibi modellerin, İHA üzerindeki kısıtlı donanımlarda ısınma sorunu yaşamadan nasıl gerçek zamanlı hızlarda tutulabileceğini merak ediyorum.
* Eğitim veri setlerinde olmayan, beklenmedik bir nesne veya farklı bir ışık kırılmasıyla karşılaşıldığında, sistemin kararsız kalıp kilitlenmesini nasıl engelleyebiliriz? Modelin bilmediği bir durumda güvenli moda geçmesi yazılımsal olarak nasıl kurgulanır?

## Kaynakça
* **OpenCV Documentation:** https://docs.opencv.org/ 
* **Ultralytics YOLOv11 Docs:** https://docs.ultralytics.com 
* **Draw.io:** https://app.diagrams.net/
