# Ortam Kurulum Adımları

Bu projede OpenCV ve NumPy kütüphanelerini kullanmak için izole bir çalışma ortamı oluşturulmuştur.

### Kullanılan Adımlar:
1. **Klasör Yapısı:** Proje için `week2` ve çıktıların kaydedileceği `outputs` klasörleri oluşturuldu.
2. **Sanal Ortam (venv):** `python -m venv venv` komutu ile kütüphanelerin çakışmaması için sanal ortam kuruldu.
3. **Aktifleştirme:** `.\venv\Scripts\activate` komutu ile sanal ortama giriş yapıldı.
4. **Kütüphane Kurulumu:** `pip install opencv-python numpy` komutları çalıştırıldı.
5. **Gereksinimler:** Kurulu olan tüm kütüphaneler `pip freeze > requirements.txt` komutu ile listelendi.

**Karşılaşılan Sorunlar ve Çözümler:**
* Başlangıçta klasör yolu OneDrive üzerinde olduğu için "sistem belirtilen yolu bulamıyor" hatası alındı, tam dosya yolu kullanılarak sorun çözüldü.