import cv2
import numpy as np

# Resmi oku ve griye çevir
img = cv2.imread('resim1.jpg')
img = cv2.resize(img, (800, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Eşikleme (Kontur bulmak için temiz bir siyah-beyaz resim şart)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV) # INV kullandım nesneler beyaz olsun diye

# 1. Konturları Bul
# cv2.RETR_EXTERNAL: Sadece en dış konturları bulur
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Analiz için orijinalin kopyasını alalım
output_img = img.copy()

# Tüm konturları alanlarına göre büyükten küçüğe sıralayalım
contours = sorted(contours, key=cv2.contourArea, reverse=True)

count = 0
for cnt in contours:
    area = cv2.contourArea(cnt)
    
    # 2. Alan Filtrelemesi: Çok küçük noktaları (gürültü) eleyelim
    if area > 500: # 500 pikselden küçükse kuş veya gürültüdür, geç.
        count += 1
        peri = cv2.arcLength(cnt, True)
        
        # 3. Bounding Box (Sınırlayıcı Kutu)
        x, y, w, h = cv2.boundingRect(cnt)
        
        # 4. Şekil Analizi (Yaklaşım algoritması)
        epsilon = 0.04 * peri
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        
        shape_name = "Poligon"
        if len(approx) == 3: shape_name = "Ucgen"
        elif len(approx) == 4:
            aspect_ratio = float(w)/h
            shape_name = "Kare" if 0.95 <= aspect_ratio <= 1.05 else "Dikdortgen"
        elif len(approx) > 10: shape_name = "Daire"

        # 5. En Büyük 3 Konturu Farklı Renkle İşaretle
        color = (0, 255, 0) # Genel yeşil
        if count == 1: color = (0, 0, 255) # 1. En büyük KIRMIZI
        elif count == 2: color = (255, 0, 0) # 2. En büyük MAVİ
        elif count == 3: color = (0, 255, 255) # 3. En büyük SARI

        # Çizimler
        cv2.drawContours(output_img, [cnt], -1, color, 2)
        cv2.rectangle(output_img, (x, y), (x + w, y + h), (255, 255, 255), 1)
        
        # Bilgileri ekrana yaz
        cv2.putText(output_img, f"{shape_name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        print(f"Nesne {count}: Alan: {area:.1f}, Cevre: {peri:.1f}, Sekil: {shape_name}")

# Göster
cv2.imshow('Kontur Analizi ve Sekil Tespit', output_img)
cv2.imwrite('outputs/5_kontur_analizi.jpg', output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()