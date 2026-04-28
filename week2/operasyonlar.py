import cv2
import numpy as np
import os

if not os.path.exists("outputs"):
    os.makedirs("outputs")

def tum_odevi_tamamla(resim_adi):
    img = cv2.imread(resim_adi)
    if img is None:
        print("Resim bulunamadı!")
        return

    # --- 1. Bilgi Alma ---
    h, w, c = img.shape
    print(f"Resim Boyutu: {w}x{h}, Piksel Sayısı: {img.size}")

    # --- 2. Yeniden Boyutlandırma ---
    # 640x480 hali
    res_640 = cv2.resize(img, (640, 480))
    cv2.imwrite("outputs/resize_640x480.jpg", res_640)
    # Genişliği 300 yapıp oranı koruma
    oran = 300.0 / w
    yeni_boyut = (300, int(h * oran))
    res_oranli = cv2.resize(img, yeni_boyut)
    cv2.imwrite("outputs/resize_oranli.jpg", res_oranli)

    # --- 3. Kırpma (ROI) ---
    # Bu sefer biraz daha içeriği olan bir yeri keselim (Örn: 200-500 arası)
    kesilmis = img[100:500, 100:500]
    cv2.imwrite("outputs/crop_roi.jpg", kesilmis)

    # --- 4. Döndürme ve Yansıtma ---
    dondur = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    yansit_yatay = cv2.flip(img, 1)
    cv2.imwrite("outputs/rotate_90.jpg", dondur)
    cv2.imwrite("outputs/flip_yatay.jpg", yansit_yatay)

    # --- 5. HSV ve Kanalları Ayırma ---
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(hsv)
    cv2.imwrite("outputs/hsv_hue.jpg", H) # Renk kanalı
    cv2.imwrite("outputs/hsv_sat.jpg", S) # Dolgunluk kanalı
    cv2.imwrite("outputs/hsv_val.jpg", V) # Parlaklık kanalı

    # --- 6. Piksel Manipülasyonu (Basit Maskeleme) ---
    # Resmin bir bölgesini (50x50'den 200x200'e kadar) siyaha boyayalım
    maskeli_resim = img.copy()
    maskeli_resim[50:200, 50:200] = [0, 0, 0] # BGR formatında siyah
    cv2.imwrite("outputs/pixel_mask.jpg", maskeli_resim)

    print("TEBRİKLER! Tüm operasyonlar tamamlandı ve kaydedildi.")

tum_odevi_tamamla("deneme.jpg")