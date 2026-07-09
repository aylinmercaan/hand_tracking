import cv2
import time
import mediapipe as mp

from mediapipe.tasks.python import vision


cap = cv2.VideoCapture(0)


options = vision.HandLandmarkerOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=vision.RunningMode.VIDEO
)

detector = vision.HandLandmarker.create_from_options(options)

HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]

pTime = 0
cTime = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, c = frame.shape
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)
    frame_timestamp_ms = int(time.time()*1000)
    results = detector.detect_for_video(mp_image, frame_timestamp_ms)

    if results.hand_landmarks:
        for handLms in results.hand_landmarks:
            points = [(int(lm.x*w), int(lm.y*h)) for lm in handLms]
            
            for start, end in HAND_CONNECTIONS:
                cv2.line(frame, points[start], points[end], (0,255,0), 2)

            for id, (cx, cy) in enumerate(points):
                if id == 4:
                    cv2.circle(frame, (cx, cy), 9, (255, 0, 0), cv2.FILLED)
                else:
                    cv2.circle(frame, (cx, cy), 5, (0,0,255), cv2.FILLED)
            
    # fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, "FPS: "+ str(int(fps)),(10,75), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 5)
    
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) &0xFF == ord("q"):
        break



detector.close()
cap.release()
cv2.destroyAllWindows()