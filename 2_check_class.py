import yaml
import os 
# Load the YAML file
with open("config.yaml", "r") as file:
    data = yaml.safe_load(file)
dataset_folder = data["JSON_FOLDER_TO_CONVERT"]

folder_train = os.path.join(dataset_folder,r"YOLODataset\labels\train")
folder_val = os.path.join(dataset_folder,r"YOLODataset\labels\val")
import os 

### check class ###
collect_class = set()
for filename in os.listdir(folder_train):
    filepath = os.path.join(folder_train, filename)
    with open (filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            line_ls = line.split(' ')
            collect_class.update(line_ls[0])
for filename in os.listdir(folder_val):
    filepath = os.path.join(folder_val, filename)
    with open (filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            line_ls = line.split(' ')
            collect_class.update(line_ls[0])

print (collect_class)