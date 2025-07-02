import os
import urllib.request

# A fonte da câmera (0 para a webcam padrão) / The camera source (0 to the standard webcam)
CAMERA_SOURCE = 0  
# Limite de confiança para detectar objetos / Limit of confidence to detect objects
CONFIDENCE_THRESHOLD = 0.95  

# Função para instalar o modelo se não estiver presente / Function to install the model if it doesn't be present
MODEL_PATH = "model/yolov8n.pt"

def install_model(model_dir="model", model_file="yolov8n.pt"):
    # Caminho completo para o modelo / Completed path to the model
    model_path = os.path.join(model_dir, model_file)

    # Verifica se a pasta "model" existe, caso contrário cria / Verify if the paste "model" exist, otherwise, it creates
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Verifica se o modelo já foi baixado / Verify if the model already has been installed
    if not os.path.exists(model_path):
        print("🔽 Baixando o modelo YOLO...")
        # URL para o modelo YOLOv8
        model_url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"
        urllib.request.urlretrieve(model_url, model_path)
        print(f"Modelo {model_file} baixado com sucesso!")
    else:
        print("Modelo já está presente.")

# Chama a função para garantir que o modelo está instalado / Call the action to guarantee that the model is installed
install_model()