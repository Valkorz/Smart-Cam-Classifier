import cv2 # Biblioteca para capturar câmera / Library used to capture the camera
from config import config
from core.camera import open_camera, release_camera
from core.detection import detect_objects
from core.display import show_frame, save_frame
from utils.alerts import send_alert

def main():
    cap = open_camera(config.CAMERA_SOURCE)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = detect_objects(frame)

        show_frame(frame, results)

        # Exemplo de ação: salvar imagem se detectar pessoas
        for r in results:
            for box in r.boxes:
                if cls == 'person' and box.conf[0] > config.CONFIDENCE_THRESHOLD:
                    save_frame(frame)
                    send_alert("Pessoa detectada!")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    release_camera(cap)

if __name__ == "__main__":
    main()