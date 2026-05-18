import os
import time
import cv2
from ultralytics import YOLO

def main():
    # Canlı takipte gecikme (latency) olmaması için en hafif olan Nano modelini seçiyoruz
    print("[İŞLEM] Gerçek zamanlı takip için YOLOv8n yükleniyor...")
    model = YOLO("yolov8n.pt")
    
    # Kamerayı başlat (0 = varsayılan dahili bilgisayar kamerası)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[HATA] Kamera açılamadı! Kameranın bağlı olduğundan emin olun.")
        return

    prev_time = 0
    print("[BAŞARILI] Kamera açıldı. Kapatmak için görüntü ekranındayken 'q' tuşuna basın.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[HATA] Kameradan görüntü alınamıyor!")
            break
            
        # Ekranın genişliğini alıp SOL / ORTA / SAĞ sınırlarını belirliyoruz
        height, width, _ = frame.shape
        sol_sinir = width // 3
        sag_sinir = (width // 3) * 2
        
        # Ekranı dikey çizgilerle görsel olarak 3'e bölüyoruz (Takip kolaylığı için)
        cv2.line(frame, (sol_sinir, 0), (sol_sinir, height), (255, 0, 0), 2)
        cv2.line(frame, (sag_sinir, 0), (sag_sinir, height), (255, 0, 0), 2)
        
        # Canlı kare üzerinde YOLO çalıştırıyoruz (stream=True hızı artırır)
        # Sadece İnsan (0) ve Araba (2) sınıflarını yakalasın
        results = model(frame, stream=True, conf=0.35, classes=[0, 2])
        
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf = float(box.conf[0])
                cls_name = model.names[int(box.cls[0])]
                
                # Nesnenin tam merkez noktasını (X ve Y) buluyoruz
                merkez_x = (x1 + x2) // 2
                merkez_y = (y1 + y2) // 2
                
                # Hafta 3'teki Yön Algoritması Entegrasyonu
                if merkez_x < sol_sinir:
                    yon = "SOL"
                    renk = (0, 0, 255) # Kırmızı
                elif merkez_x > sag_sinir:
                    yon = "SAG"
                    renk = (0, 255, 255) # Sarı
                else:
                    yon = "ORTA"
                    renk = (0, 255, 0) # Yeşil
                
                # Sınır kutusunu ve merkez noktasını çiz
                cv2.rectangle(frame, (x1, y1), (x2, y2), renk, 2)
                cv2.circle(frame, (merkez_x, merkez_y), 5, (0, 0, 255), -1)
                
                # Canlı yön etiketini yaz
                label = f"{cls_name} [{yon}]"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, renk, 2)
        
        # Anlık FPS Hesaplama (Ödev İsteği)
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        
        # Sol üste FPS değerini yazdır
        cv2.putText(frame, f"FPS: {int(fps)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Canlı ekranı göster
        cv2.imshow("YOLOv8 Canli Hedef Takibi", frame)
        
        # 'q' tuşuna basılırsa kamerayı kapat
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()