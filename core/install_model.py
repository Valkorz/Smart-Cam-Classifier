import os
import urllib.request

def instal_model(model_dir="model", model_file="yolov8n.pt"):
    # Define o caminho completo para o modelo / Define the complete path to the model
    model_path = os.path.join(model_dir, model_file)

    # Cria a pasta model se não existir / Create the model paste if it doesn't exist
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Verifica se o modelo já existe / Verify if the model already exist
    if not os.path.exists(model_path):
        print(" Baixando modelo YOLO...")
        # URL do modelo / URL of the model
        model_url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"
        urllib.request.urlretrieve(model_url, model_path)
        print(f"Modelo {model_file} baixado com sucesso!")
    else:
        print(" Modelo já está presente.")