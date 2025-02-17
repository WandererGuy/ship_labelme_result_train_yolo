from ultralytics import YOLO
import yaml
import os
# Load the YAML file
with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)
dataset_folder = data["JSON_FOLDER_TO_CONVERT"]
epoch_train = data["EPOCH_TRAIN"]

PRETRAIN_MODEL_PATH = data["PRETRAIN_MODEL_PATH"]
YAML_FILE_PATH = r"YOLODataset\dataset.yaml"
if __name__ == '__main__':
    model = YOLO(PRETRAIN_MODEL_PATH)  # load a pretrained model (recommended for training)
    import torch 
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print (device)
    model.to(device)
    results = model.train(data=YAML_FILE_PATH, epochs=epoch_train, imgsz=640, device=device, patience=10)
