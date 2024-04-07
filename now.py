import cv2
import numpy as np

def process_frame(frame, face_cascade, sunglasses):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_region = frame[y:y+h, x:x+w]
        sunglasses_resized = cv2.resize(sunglasses, (w, h), interpolation=cv2.INTER_AREA)
        face_region_with_sunglasses = cv2.add(face_region, sunglasses_resized)
        frame[y:y+h, x:x+w] = face_region_with_sunglasses

    return frame

def main():
    # Load the sunglasses image
    try:
        sunglasses = cv2.imread("sunglasses.png", cv2.IMREAD_UNCHANGED)
    except Exception as e:
        print(f"Error loading sunglasses image: {e}")
        return

    # Create a face detection model
    try:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    except Exception as e:
        print(f"Error loading face detection model: {e}")
        return

    # Set up the video capture
    try:
        cap = cv2.VideoCapture(0)
    except Exception as e:
        print(f"Error setting up video capture: {e}")
        return

    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame from video capture")
            break

        # Process the frame
        frame_with_sunglasses = process_frame(frame, face_cascade, sunglasses)

        # Display the frame with sunglasses overlay
        cv2.imshow("Sunglasses Overlay", frame_with_sunglasses)

        # Exit if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
