import cv2
import numpy as np

# Load the sunglasses image
sunglasses = cv2.imread("sunglasses.png", cv2.IMREAD_UNCHANGED)

# Create a face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Set up the video capture
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop through all detected faces
    for (x, y, w, h) in faces:
        # Extract the face region
        face_region = frame[y:y+h, x:x+w]

        # Resize the sunglasses image to match the face region size
        sunglasses_resized = cv2.resize(sunglasses, (w, h), interpolation=cv2.INTER_AREA)

        # Overlay the sunglasses on the face region
        face_region_with_sunglasses = cv2.add(face_region, sunglasses_resized)

        # Replace the face region with the sunglasses overlay
        frame[y:y+h, x:x+w] = face_region_with_sunglasses

    # Display the frame with sunglasses overlay
    cv2.imshow("Sunglasses Overlay", frame)

    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
