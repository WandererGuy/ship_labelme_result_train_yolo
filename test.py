import os 
import shutil 
folder  = "NAM_ALL_REFINED"
import json

for filename in os.listdir(folder):
    if filename.endswith(".json"):
        # Open and read the JSON file
        path = os.path.join(folder, filename)
        with open(path, 'r') as file:
            data = json.load(file)
            data["imagePath"] = path.replace(".json", ".jpg")
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)