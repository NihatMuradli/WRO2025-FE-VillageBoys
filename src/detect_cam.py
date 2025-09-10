import cv2
import pytesseract
import time
from picamera2 import Picamera2

# Initialize Picamera2
picam2 = Picamera2()

# Configure the camera for 640x480 resolution with autofocus enabled
camera_config = picam2.create_video_configuration(main={"size": (1920, 1080)})
picam2.configure(camera_config)

# Enable autofocus (if supported)

picam2.start()

# Allow the camera to warm up
time.sleep(1)

def process_frame(frame):
    """
    Process the frame for OCR detection using pytesseract.
    """
    # Manually rotate the frame (180 degrees rotation)

    # Convert frame to RGB as required by Tesseract
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Use pytesseract to detect text in the image
    text = pytesseract.image_to_string(rgb_image)

    # Show the detected text
    print(f"Detected Text:\n{text}")

    return frame

try:
    while True:
        # Capture the frame
        frame = picam2.capture_array()

        # Process the frame for text detection
        processed_frame = process_frame(frame)

        # Display the frame
        cv2.imshow("Frame", processed_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Clean up the resources
    picam2.stop()
    cv2.destroyAllWindows()
