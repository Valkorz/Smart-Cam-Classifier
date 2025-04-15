import cv2
import os
import config.config as config

def show_frame(frame, results):
    annotated_frame = results[0].plot()
    cv2.imshow('SmartCam', annotated_frame)

def save_frame(frame):
    if config.SAVE_FRAMES:
        if not os.path.exists(config.FRAME_SAVE_PATH):
            os.makedirs(config.FRAME_SAVE_PATH)
        filename = os.path.join(config.FRAME_SAVE_PATH, 'frame_saved.jpg')
        cv2.imwrite(filename, frame)