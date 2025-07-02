import cv2

def show_frame(frame, results):
    annotated_frame = results[0].plot()
    cv2.imshow('SmartCam', annotated_frame)