import os
import cv2
from ultralytics import YOLO

def main():
    # Çıktıların week4/outputs klasörüne gitmesini garantiye alıyoruz
    os.makedirs("week4/outputs", exist_ok=True)
    
    # Bu bölümde Nano'dan bir tık daha güçlü olan Small (s) modelini deneyimliyoruz
    print("[İŞLEM] YOLOv8s modeli yükleniyor...")
    model = YOLO("yolov8s.pt")
    
    # Klasöründeki hazır bus.jpg resmini girdi olarak veriyoruz
    image_path = "bus.jpg" 
    
    # İHA senaryosu simulasyonu: Modelin bildiği 80 sınıftan sadece bizimkilere odaklanıyoruz
    # COCO veri setinde: 0 = person (insan), 5 = bus (otobüs)
    target_classes = [0, 5] 
    
    # Güven eşiği (Confidence Threshold)
    # Modelin bir tahmini ekrana çizmesi için en az ne kadar emin olması gerektiğini söyler.
    conf_threshold = 0.25 
    
    print(f"[İŞLEM] Filtreli model çıkarımı başlatılıyor (Gven Eşiği: {conf_threshold})...")
    results = model(image_path, conf=conf_threshold, classes=target_classes)
    
    for result in results:
        frame = result.orig_img.copy()
        boxes = result.boxes
        
        print(f"\n--- Filtrelenmiş ve Analiz Edilen Nesneler ({len(boxes)} adet) ---")
        for box in boxes:
            # Kutunun koordinatlarını alıp tam sayıya çeviriyoruz
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]
            
            # Kutunun piksel cinsinden genişlik (Width) ve yükseklik (Height) hesabı
            # İHA sistemlerinde hedefin boyutuna bakarak uzaklık tahmini yapmak için burası kritiktir!
            width = x2 - x1
            height = y2 - y1
            
            print(f"Hedef: {cls_name} | Güven: {conf:.2f} | Piksel Boyutu: {width}x{height}")
            
            # Görsel üzerine yeşil renkli sınır kutusu çizimi
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Ödev İsteği: Sınıf adı, confidence değeri ve bounding box boyutlarını yazdırıyoruz
            label = f"{cls_name} {conf:.2f} ({width}x{height})"
            
            # Metnin arkasına yeşil bir şerit çekerek okunabilirliği artırıyoruz
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            cv2.rectangle(frame, (x1, y1 - h - 5), (x1 + w, y1), (0, 255, 0), -1)
            
            # Şeritin üzerine siyah yazıyla bilgileri basıyoruz
            cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
            
        # Çıktıyı kaydediyoruz
        output_name = f"week4/outputs/filtre_cikti_conf_{int(conf_threshold*100)}.jpg"
        cv2.imwrite(output_name, frame)
        print(f"\n[BAŞARILI] Filtrelenmiş görsel kaydedildi: {output_name}")

if __name__ == "__main__":
    main()