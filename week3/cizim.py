import cv2
import numpy as np

dosya_adi = 'resim1.jpg' 
img = cv2.imread(dosya_adi)

if img is None:
    print("Hata: Fotoğraf bulunamadı! Dosya adını kontrol et.")
else:
    # Ekran sığması için makul bir boyuta çekelim
    img = cv2.resize(img, (800, 600))

    # --- BÖLÜM 2 İSTERLERİ ---

    # 1. DİKDÖRTGEN (Bounding Box): Siyah arabayı kutuya alalım
    # (resim, sol_ust, sag_alt, renk_bgr, kalinlik)
    cv2.rectangle(img, (70, 360), (280, 580), (0, 255, 0), 3)

    # 2. DAİRE (Merkez Noktası): Arabanın tam ortasına kırmızı nokta
    # (resim, merkez, yaricap, renk_bgr, kalinlik_-1_dolu)
    cv2.circle(img, (175, 470), 6, (0, 0, 255), -1)

    # 3. POLİGON (Çokgen): Binanın bir kısmını mor bir çokgenle işaretleyelim
    # Köşe noktalarını belirliyoruz
    pts = np.array([[350, 100], [550, 100], [600, 250], [300, 250]], np.int32)
    # (resim, noktalar, kapali_mi, renk, kalinlik)
    cv2.polylines(img, [pts], isClosed=True, color=(255, 0, 255), thickness=2)

    # 4. ÇİZGİ: Ekranın ortasına bir nişangah (Crosshair)
    # Yatay ve dikey çizgiler
    cv2.line(img, (380, 300), (420, 300), (255, 255, 0), 2) # Turkuaz benzeri
    cv2.line(img, (400, 280), (400, 320), (255, 255, 0), 2)

    # 5. METİN: Türkçe karaktersiz, fontu ve boyutu ayarlanmış metinler
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Hedef bilgisi
    cv2.putText(img, "HEDEF: ARAC", (70, 350), font, 0.7, (0, 255, 0), 2)
    # Boyut bilgisi (İsterlerde vardı)
    cv2.putText(img, "BOYUT: 210x220", (70, 330), font, 0.5, (255, 255, 255), 1)
    # Bilgi mesajı
    cv2.putText(img, "Bolum 2: Cizim Testi", (10, 30), font, 0.8, (255, 255, 255), 2)

    # --- GÖSTER VE KAYDET ---
    cv2.imshow('Bolum 2: Tum Cizimler', img)
    
    # Çıktıyı outputs klasörüne kaydet (Klasörün olduğundan emin ol)
    cv2.imwrite('outputs/2_cizim_tam_sonuc.jpg', img)

    print("Çizimler başarıyla yapıldı. Kapatmak için bir tuşa bas.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()