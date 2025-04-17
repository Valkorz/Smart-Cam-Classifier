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
                cls_id = int(box.cls[0])
                cls_name = r.names[cls_id]
                confidence = box.conf[0]

                print(f"Detecção: {cls_name} com confiança de {confidence: .2f}")

                if confidence > config.CONFIDENCE_THRESHOLD:
                    save_frame(frame)
                    send_alert(f"Objeto detectado: {cls_name}")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Encerrando...")
            break
    release_camera(cap)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()