import cv2
import pytesseract

# Path to Tesseract executable (for Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to video file
video_path = 'your_video.mp4'

# Open video file
cap = cv2.VideoCapture(video_path)

# Initialize OCR engine
ocr_engine = pytesseract.image_to_string

# Process video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract text from frame using OCR
    text = ocr_engine(gray)

    # Print extracted text
    print(text)

    # Display frame with detected text (optional)
    cv2.imshow('Frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
