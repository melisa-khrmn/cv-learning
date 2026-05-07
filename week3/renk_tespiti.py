import cv2
import numpy as np

# Resmi yükle
img = cv2.imread('resim2.jpg') # Kendi dosya adınla değiştir
img = cv2.resize(img, (800, 600))

# 1. BGR'den HSV'ye Dönüştür
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 2. GÜNCEL RENK ARALIKLARI (Bu fotoğraftaki balonlara özel)
# Mavi/Turkuaz Aralığı (Biraz daha genişlettik)
lower_blue = np.array([85, 100, 100])
upper_blue = np.array([130, 255, 255])

# Sarı Aralığı
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([35, 255, 255])

# 3. Maskeleri Oluştur
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

# 4. Morfolojik Temizlik (Küçük lekeleri siler)
kernel = np.ones((5,5), np.uint8)
mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)
mask_yellow = cv2.morphologyEx(mask_yellow, cv2.MORPH_OPEN, kernel)

def nesne_bul_ve_isaretle(mask, color_name, draw_color):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count = 0
    for cnt in contours:
        # Alanı biraz küçülttük ki tüm balonları yakalasın
        if cv2.contourArea(cnt) > 300: 
            count += 1
            x, y, w, h = cv2.boundingRect(cnt)
            
            # Moment ile merkez hesaplama
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                
                # Çizimler
                cv2.rectangle(img, (x, y), (x + w, y + h), draw_color, 2)
                cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
                cv2.putText(img, f"{color_name}", (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, draw_color, 1)
    return count

# Tespitleri yap
mavi_sayisi = nesne_bul_ve_isaretle(mask_blue, "Mavi", (255, 0, 0))
sari_sayisi = nesne_bul_ve_isaretle(mask_yellow, "Sari", (0, 255, 255))

# Bilgi paneli
cv2.rectangle(img, (10, 10), (250, 60), (0,0,0), -1) # Arka plan siyah kutu
cv2.putText(img, f"Mavi Balon: {mavi_sayisi}", (20, 30), 2, 0.6, (255, 100, 100), 1)
cv2.putText(img, f"Sari Balon: {sari_sayisi}", (20, 50), 2, 0.6, (100, 255, 255), 1)

cv2.imshow('Final: Renkli Balon Tesbiti', img)
cv2.imshow('Mavi Maske Filtresi', mask_blue)

# Tespit edilen final görüntüsünü ve maskeyi kaydet
cv2.imwrite('outputs/6_renk_tespiti_final.jpg', img)
cv2.imwrite('outputs/6_mavi_maske.jpg', mask_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()