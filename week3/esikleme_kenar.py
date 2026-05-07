import cv2
import numpy as np

img = cv2.imread('resim1.jpg')
img = cv2.resize(img, (600, 400))

# 1. ADIM: Gri Tonlamaya Çevirme (Eşikleme ve Kenar bulma gri resim üzerinde yapılır)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. ADIM: Üç Farklı Eşikleme Yöntemi
# Binary: Sabit bir değer (127) belirleriz.
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Otsu: En iyi eşik değerini görüntünün ışık dağılımına göre kendi hesaplar.
_, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Adaptive: Resmin her bölgesine özel eşik belirler (Gölge varsa en iyisidir).
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 3. ADIM: Filtrelemenin Kenar Tespitine Etkisi
# Ham (filtresiz) resimde kenarlar
edges_raw = cv2.Canny(gray, 100, 200)

# Filtreli (Bilateral) resimde kenarlar (Gürültü azalır, kenarlar netleşir)
blurred = cv2.bilateralFilter(gray, 9, 75, 75)
edges_filtered = cv2.Canny(blurred, 100, 200)

# SONUÇLARI GÖSTER
cv2.imshow('1-Binary (Sabit)', binary)
cv2.imshow('2-Otsu (Otomatik)', otsu)
cv2.imshow('3-Adaptive (Bolgesel)', adaptive)
cv2.imshow('4-Kenar (Filtresiz)', edges_raw)
cv2.imshow('5-Kenar (Filtreli)', edges_filtered)

# Tüm eşikleme ve kenar tespiti varyasyonlarını kaydet
cv2.imwrite('outputs/3_1_binary_threshold.jpg', binary)
cv2.imwrite('outputs/3_2_otsu_threshold.jpg', otsu)
cv2.imwrite('outputs/3_3_adaptive_threshold.jpg', adaptive)
cv2.imwrite('outputs/3_4_canny_raw.jpg', edges_raw)
cv2.imwrite('outputs/3_5_canny_filtered.jpg', edges_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()