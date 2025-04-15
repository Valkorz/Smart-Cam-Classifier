from ultralytics import YOLO
import config.config as config

model = YOLO(config.MODEL_PATH)

def detect_objects(frame):
    results = model(frame)
    return results