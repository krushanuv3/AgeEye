import cv2
from deepface import DeepFace

def get_age(face):
    try:
        # Use DeepFace to analyze the age
        analysis = DeepFace.analyze(face, actions=['age'], enforce_detection=False)
        return analysis[0]['age']  # Return the age of the first detected face
    except Exception as e:
        print(f"Error in age detection: {e}")
        return None

# Load Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale (Haar Cascade works better with grayscale)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    # Process each detected face
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        age = get_age(face)

        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display age above the rectangle
        if age is not None:
            cv2.putText(frame, f'Age: {age}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the frame with detected faces
    cv2.imshow('Age Detection', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
