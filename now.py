import cv2
import numpy as np

def overlay_sunglasses(face_region, sunglasses):
    alpha_sunglasses = sunglasses[:, :, 3] / 255.0
    alpha_face = 1.0 - alpha_sunglasses

    for c in range(0, 3):
        face_region[:, :, c] = (alpha_sunglasses * sunglasses[:, :, c] +
                               alpha_face * face_region[:, :, c])

def process_frame(frame, face_cascade, sunglasses):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        sunglasses_resized = cv2.resize(sunglasses, (w, h), interpolation=cv2.INTER_AREA)
        overlay_sunglasses(frame[y:y+h, x:x+w], sunglasses_resized)

    return frame

def main():
    sunglasses = cv2.imread("sunglasses.png", cv2.IMREAD_UNCHANGED)
    if sunglasses is None:
        print("Error loading sunglasses image")
        return
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    if face_cascade.empty():
        print("Error loading face detection model")
        return

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error setting up video capture")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error reading frame from video capture")
                break

            frame_with_sunglasses = process_frame(frame, face_cascade, sunglasses)
            cv2.imshow("Sunglasses Overlay", frame_with_sunglasses)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
