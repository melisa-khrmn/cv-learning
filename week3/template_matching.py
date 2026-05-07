import cv2
import numpy as np

# 1. Görüntüyü yükle
img_rgb = cv2.imread('resim1.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# 2. Şablonu Kesme (Örnek: Fotoğraftaki bir balonu veya pencereyi koordinatla kesiyoruz)
# Fotoğrafına göre bu koordinatları (y1:y2, x1:x2) değiştirebilirsin
template = img_gray[250:350, 300:380] 
w, h = template.shape[::-1]

# 3. Şablon Eşleme Uygula
# TM_CCOEFF_NORMED: En kararlı sonuç veren yöntemlerden biridir
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# 4. Eşik Değeri Belirle (Birden fazla eşleşme bulmak için)
threshold = 0.8 # %80 benzerlik üzerini kabul et
loc = np.where(res >= threshold)

# 5. Bulunan Tüm Eşleşmeleri İşaretle
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

cv2.imshow('Kesilen Sablon', template)
cv2.imshow('Bulunan Eslesmeler', img_rgb)

# Bulunan eşleşmeleri ve kesilen şablonu kaydet
cv2.imwrite('outputs/7_template_sonuc.jpg', img_rgb)
cv2.imwrite('outputs/7_kesilen_sablon.jpg', template)

cv2.waitKey(0)
cv2.destroyAllWindows()