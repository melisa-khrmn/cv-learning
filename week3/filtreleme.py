import cv2
import numpy as np

dosya_adi = 'resim1.jpg' 

img = cv2.imread(dosya_adi)

if img is None:
    print("Hata: Fotoğraf bulunamadı!")
else:
    # Boyutu manuel verelim: Örneğin her pencere 600x400 olsun
    genislik, yukseklik = 600, 400
    img = cv2.resize(img, (genislik, yukseklik)) 

    # Filtreler
    gaussian = cv2.GaussianBlur(img, (7, 7), 0) # Kernel'ı 7x7 yaptım, fark daha net olsun
    median = cv2.medianBlur(img, 7) # Kernel'ı 7 yaptım
    bilateral = cv2.bilateralFilter(img, 15, 80, 80) # Daha güçlü bir bilateral

    # Pencereleri oluştur ve isimlendir
    cv2.namedWindow('1-Orijinal')
    cv2.namedWindow('2-Gaussian')
    cv2.namedWindow('3-Median')
    cv2.namedWindow('4-Bilateral')

    # Pencereleri ekranın dört köşesine taşı (x, y koordinatları)
    cv2.moveWindow('1-Orijinal', 50, 50)       # Sol Üst
    cv2.moveWindow('2-Gaussian', 700, 50)      # Sağ Üst
    cv2.moveWindow('3-Median', 50, 500)       # Sol Alt
    cv2.moveWindow('4-Bilateral', 700, 500)    # Sağ Alt

    # Görüntüleri bas
    cv2.imshow('1-Orijinal', img)
    cv2.imshow('2-Gaussian', gaussian)
    cv2.imshow('3-Median', median)
    cv2.imshow('4-Bilateral', bilateral)

    # Tüm filtreleme varyasyonlarını ayrı ayrı kaydet
    cv2.imwrite('outputs/1_1_filtre_gaussian.jpg', gaussian)
    cv2.imwrite('outputs/1_2_filtre_median.jpg', median)
    cv2.imwrite('outputs/1_3_filtre_bilateral.jpg', bilateral)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()