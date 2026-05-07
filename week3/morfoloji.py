import cv2
import numpy as np

# Resmi gri tonlamada oku ve boyutlandır
img = cv2.imread('resim1.jpg', 0)
img = cv2.resize(img, (600, 400))

# Binary (Siyah-Beyaz) hale getir
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Kernel Tanımlama (5x5 bir matris)
# Boyutu (7,7) yaparsan etkinin çok daha sert olduğunu görürsün
kernel = np.ones((5,5), np.uint8)

# 1. Erosion (Aşındırma): Beyaz alanları küçültür, küçük gürültüleri siler
erosion = cv2.erode(thresh, kernel, iterations=1)

# 2. Dilation (Genişletme): Beyaz alanları büyütür, kopuk çizgileri birleştirir
dilation = cv2.dilate(thresh, kernel, iterations=1)

# 3. Opening (Açma): Önce Aşındırma -> Sonra Genişletme (Dış gürültü temizleme)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# 4. Closing (Kapama): Önce Genişletme -> Sonra Aşındırma (İç boşluk doldurma)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Görüntüleri Yan Yana Göster
cv2.imshow('Orijinal Binary', thresh)
cv2.imshow('Asindirma', erosion)
cv2.imshow('Genisletme', dilation)
cv2.imshow('Acma (Gurultu Silme)', opening)
cv2.imshow('Kapama (Bosluk Doldurma)', closing)

# Tüm morfolojik sonuçları tek tek kaydet
cv2.imwrite('outputs/4_morfoloji_erosion.jpg', erosion)
cv2.imwrite('outputs/4_morfoloji_dilation.jpg', dilation)
cv2.imwrite('outputs/4_morfoloji_opening.jpg', opening)
cv2.imwrite('outputs/4_morfoloji_closing.jpg', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()