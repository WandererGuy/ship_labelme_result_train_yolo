import yaml 
import os 
import time 
import shutil 
if os.path.exists("labels"):
    shutil.rmtree("labels")
if os.path.exists("refined"):
    os.rename("refined", "labels")
if os.path.exists("NAM_ALL_REFINED/YOLODataset/labels"):
    shutil.rmtree("NAM_ALL_REFINED/YOLODataset/labels")
if os.path.exists("./YOLODataset"):
    shutil.rmtree("./YOLODataset")

time.sleep(3)
shutil.copytree("labels", "NAM_ALL_REFINED/YOLODataset/labels")
time.sleep(3)
shutil.move("NAM_ALL_REFINED/YOLODataset", "./")