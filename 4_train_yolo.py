from ultralytics import YOLO
import yaml
import os
# Load the YAML file
with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)
dataset_folder = data["JSON_FOLDER_TO_CONVERT"]
epoch_train = data["EPOCH_TRAIN"]

PRETRAIN_MODEL_PATH = data["PRETRAIN_MODEL_PATH"]
YAML_FILE_PATH = os.path.join(dataset_folder, r"YOLODataset\dataset.yaml")
if __name__ == '__main__':
    model = YOLO(PRETRAIN_MODEL_PATH)  # load a pretrained model (recommended for training)
    results = model.train(data=YAML_FILE_PATH, epochs=epoch_train, imgsz=640)
