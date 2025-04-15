import cv2

def open_camera(source):
    cap = cv2.ViideoCapture(source)
    if not cap.isOpened():
        raise Exception("Erro ao abrir a câmera")
    # Função para caso não consiga abrir a câmera, ele manda essa mensagem / Function to print an alert in case of the camera doesn't open
    return cap
def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()