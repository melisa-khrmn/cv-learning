from ultralytics import YOLO

def main():
    # 1. Hazır YOLOv8 nano modelini yüklüyoruz
    model = YOLO("yolov8n.pt")

    # 2. Modeli kendi su şişesi veri setimizle eğitiyoruz
    # data="data.yaml" -> Az önce düzenlediğimiz ayar dosyasını gösterir
    # epochs=20 -> Resimleri 20 tur döndürerek eğitir
    model.train(data="data.yaml", epochs=20, imgsz=640)

if __name__ == '__main__':
    main()