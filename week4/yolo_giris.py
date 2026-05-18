import os
import cv2
from ultralytics import YOLO

def main():
    os.makedirs("week4/outputs", exist_ok=True)
    
    print("[İŞLEM] Model yükleniyor (İlk seferde internetten indirilir)...")
    model = YOLO("yolov8n.pt")
    
    image_source = "https://ultralytics.com/images/bus.jpg" 
    
    print(f"[İŞLEM] Model tahmini (Inference) başlatılıyor: {image_source}")
    results = model(image_source)
    
    for result in results:
        annotated_frame = result.plot()
        output_path = "week4/outputs/yolo_giris_cikti.jpg"
        cv2.imwrite(output_path, annotated_frame)
        print(f"[BAŞARILI] Çıktı görseli kaydedildi: {output_path}")
        
        boxes = result.boxes
        print("\n--- TESPİT EDİLEN NESNE DETAYLARI ---")
        for box in boxes:
            xyxy = box.xyxy[0].tolist()
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]
            
            print(f"Sınıf: {cls_name} (ID: {cls_id}) | Güven Skoru: {conf:.2f} | Koordinatlar: {[round(x, 1) for x in xyxy]}")

if __name__ == "__main__":
    main()