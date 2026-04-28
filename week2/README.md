UYGULANAN FONKSİYONLAR

gri_versiyon (Gri Tonlama): Resimdeki renkleri çıkarıp sadece parlaklık değerlerini bırakır. Nesne kenarlarını daha hızlı bulmak için resmi sadeleştirir.

resize_640x480 (Standart Boyutlandırma): Resmi tam 640x480 boyutuna getirir. Yapay zeka modellerinin hepsine aynı boyutta veri girişi sağlamak için kritiktir.

resize_oranli (En-Boy Oranlı Boyutlandırma): Resmi sündürmeden, genişliğini 300 piksele düşürür. Görüntüdeki nesnelerin şeklinin bozulmamasını sağlar.

crop_roi (Kırpma / İlgi Alanı): Resmin sadece istenen bölgesini kesip ayırır. Gereksiz kısımları atarak işlem hızını artırır.

rotate_90 (Döndürme): Resmi 90 derece sağa çevirir. Farklı açılardan gelen kamera görüntülerini düzeltmeye yarar.

flip_yatay (Yansıtma): Resmi aynadaki görüntüsü gibi ters çevirir. Veri setini çeşitlendirerek algoritmanın nesneyi her yönden tanımasını sağlar.

hsv_hue (Renk Özü - H): Resimdeki nesnelerin sadece hangi renk olduğunu saklar. Işık değişse de nesnenin rengini bu kanaldan takip ederiz.

hsv_sat (Dolgunluk - S): Rengin ne kadar canlı veya ne kadar soluk olduğunu gösterir.

hsv_val (Parlaklık - V): Resmin ne kadar ışık aldığını, nerelerin karanlık nerelerin aydınlık olduğunu gösterir.

pixel_mask (Piksel Manipülasyonu): Resmin bir kısmını elle siyaha boyar. Belirli bir bölgeyi gizlemek veya maskelemek için kullanılır.