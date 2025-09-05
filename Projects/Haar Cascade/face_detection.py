import numpy as np
import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_classifier = cv2.CascadeClassifier(
    r"C:\Users\bhara\Downloads\haarcascade_frontalface_default.xml"
)

# Load the image
image = cv2.imread(r"C:\Users\bhara\Downloads\istockphoto-507995592-612x612.jpg")

# checking of the image has loaded properly or not
if image is None:
    print("Could not open or find the image.")
    exit()  # exits if the image is not found

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# Checks if any faces were detected
if len(faces) == 0:
    print("No faces found")
else:
    # Draw rectangles around the detected faces
    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 255), 2)
    # display the output image with detected faces
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)  # waits for a key press to close the window

# close all the opened windows
cv2.destroyAllWindows()
