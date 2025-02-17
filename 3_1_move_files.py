import yaml 

with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)

import os 
import shutil 
os.rename("refined", "labels")
shutil.rmtree("NAM_ALL_REFINED/YOLODataset/labels")
shutil.copytree("labels", "NAM_ALL_REFINED/YOLODataset")
shutil.move("NAM_ALL_REFINED/YOLODataset", "./")