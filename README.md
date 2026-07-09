# El ve Parmak Ucu Takip Sistemi (Hand & Fingertip Tracking)

Gerçek zamanlı kamera görüntüsü üzerinden **MediaPipe Tasks API** kullanarak el iskeletini tespit eden ve başparmak ucunu vurgulayan bir bilgisayarlı görü (computer vision) projesi.

## Özellikler

- Web kamerasından gerçek zamanlı görüntü işleme
- El iskeleti (21 nokta) tespiti ve çizimi
- Başparmak ucunun (landmark id: 4) özel olarak vurgulanması
- Anlık FPS (kare/saniye) göstergesi
- Elle çizilen iskelet bağlantıları (harici drawing modülüne bağımlı değil)

## Kullanılan Teknolojiler

- [Python] 3.14+
- [OpenCV] - kamera görüntüsü işleme ve çizim
- [MediaPipe Tasks API] - el landmark tespiti

## Çalıştırma

- Kamera penceresi açılacak ve elinizi gösterdiğinizde iskelet çizgileri ve eklem noktaları görünecektir.
- Çıkmak için `q` tuşuna basın.

## Nasıl Çalışır?

1. OpenCV ile kameradan her karede görüntü alınır.
2. Görüntü, MediaPipe'ın beklediği `mp.Image` formatına dönüştürülür.
3. `HandLandmarker` modeli, eldeki 21 anahtar noktanın (parmak eklemleri, bilek vb.) koordinatlarını döndürür.
4. Bu noktalar `cv2.line` ve `cv2.circle` ile görüntü üzerine elle çizilir (harici `drawing_utils` modülüne ihtiyaç duyulmaz).
5. Başparmak ucu (id: 4) farklı bir renkle vurgulanır.
6. Kareler arası geçen süre ölçülerek anlık FPS ekrana yazdırılır.

## Bilinen Sorunlar / Notlar

- Bazı MediaPipe sürümleri (özellikle Windows üzerinde) `mediapipe.framework` ve `mediapipe.solutions` alt modüllerini içermeyebilir. Bu yüzden bu projede çizim işlemi tamamen elle (manuel) yapılmıştır, herhangi bir `mediapipe.solutions.drawing_utils` bağımlılığı yoktur.

## Lisans

Bu proje eğitim amaçlıdır ve serbestçe kullanılabilir.
