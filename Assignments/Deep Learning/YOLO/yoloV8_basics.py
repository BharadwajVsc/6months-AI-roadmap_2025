from ultralytics import YOLO
import numpy as np

# loading the pretrained model
model = YOLO("yolov8n.pt", "v8")

# predicting on an image
detection_output = model.predict(
    source="practice_codes/deep_learning/yolo/pexels-pixabay-210182.jpg",
    conf=0.25,
    save=True,
)  # conf is used to set the confidence threshold

print(detection_output)
