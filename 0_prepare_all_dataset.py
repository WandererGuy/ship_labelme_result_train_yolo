import os 

def find_all_image_paths(folder_path):
    # List of common video file extensions
    video_extensions = ['.jpg', '.png', '.jpeg', '.jpg']
    video_paths = []
    
    # Walk through the folder to find video files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in video_extensions):
                video_paths.append(os.path.join(root, file))
    
    return video_paths

import shutil
import uuid
from tqdm import tqdm
def main():
    """
    make_labelme_result from same name files (json and image files) from different folder 
    """
    for folder_path in ["NAM_ALL_REFINED", "YOLODataset"]:
        if os.path.exists(folder_path):
            # Remove the folder and its contents
            shutil.rmtree(folder_path)
            print(f"The folder {folder_path} has been removed.")
    import yaml 
    with open("config.yaml", "r") as file:
        data = yaml.safe_load(file)
    SOURCE_FOLDER = data["SOURCE_FOLDER"]
    dest_folder = "NAM_ALL_REFINED"
    os.makedirs(dest_folder, exist_ok=True)
    image_ls = find_all_image_paths(SOURCE_FOLDER)
    print ("total image: ", len(image_ls))
    t = {}
    for path in image_ls:
        if path.endswith(".jpg"):
            t[path] = path.replace(".jpg", ".json")
            continue
        if path.endswith(".png"):
            t[path] = path.replace(".png", ".json")
            continue

    for image_path, json_path in tqdm(t.items(), total = len(t)):
        new_name = str(uuid.uuid4())
        shutil.copy(image_path, os.path.join(dest_folder, new_name) + ".jpg")
        shutil.copy(json_path, os.path.join(dest_folder, new_name) + ".json")

    print (len(os.listdir(dest_folder)))

if __name__ == "__main__":
    main()