import cv2
import numpy as np
import time

# Webcam akışını başlat
cap = cv2.VideoCapture(0)
pTime = 0

# TAKİP EDİLECEK RENK (Burayı elindeki nesneye göre ayarla!)
# Örnek: Parlak Turuncu/Sarı bir nesne için
lower_color = np.array([5, 100, 100])
upper_color = np.array([25, 255, 255])

while True:
    success, frame = cap.read()
    if not success: break

    # OPTİMİZASYON: Çözünürlüğü düşürmek FPS'i doğrudan artırır
    frame = cv2.resize(frame, (640, 480))
    h, w, _ = frame.shape
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    # Gürültü temizleme (Opening işlemi)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    nesne_sayisi = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > 800:
            nesne_sayisi += 1
            x, y, w_box, h_box = cv2.boundingRect(cnt)
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                
                # --- YÖN HESAPLAMA ---
                if cX < (w // 3): yon = "SOLDA"
                elif cX > (2 * w // 3): yon = "SAGDA"
                else: yon = "ORTADA"
                
                # İşaretlemeler
                cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
                cv2.putText(frame, f"HEDEF {yon}", (x, y - 10), 1, 1.5, (0, 255, 0), 2)
                cv2.circle(frame, (cX, int(M["m01"] / M["m00"])), 5, (255, 255, 255), -1)

    # FPS Hesaplama
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    # Bilgi ekranı
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), 1, 1.5, (255, 0, 0), 2)
    cv2.putText(frame, f"Nesne: {nesne_sayisi}", (10, 60), 1, 1.5, (255, 0, 0), 2)
    
    # Kılavuz çizgileri
    cv2.line(frame, (w // 3, 0), (w // 3, h), (200, 200, 200), 1)
    cv2.line(frame, (2 * w // 3, 0), (2 * w // 3, h), (200, 200, 200), 1)

    cv2.imshow("IHA Gercek Zamanli Takip", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # 'q' ile çıkış
        # Çıkış yapmadan önce son kareyi kaydet
        cv2.imwrite('outputs/8_gercek_zamanli_takip.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()