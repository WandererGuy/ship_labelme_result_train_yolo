import yaml
import os 
import time 
# Load the YAML file
def main():
        """
        replace one label with another in yolo train/val folder
        """
        with open("config.yaml", "r") as file:
            data = yaml.safe_load(file)
        dataset_folder = data["JSON_FOLDER_TO_CONVERT"]
        dest_folder_train = data["dest_folder_train"]
        dest_folder_val = data["dest_folder_val"]
        class_need_replace_ls = data["class_need_replace_ls"]
        import shutil
        class_replace_in = data["class_replace_in"]
        if os.path.exists(dest_folder_train):
            shutil.rmtree(dest_folder_train)
        if os.path.exists(dest_folder_val):
            shutil.rmtree(dest_folder_val)

        folder_train = os.path.join(dataset_folder,r"YOLODataset\labels\train")
        folder_val = os.path.join(dataset_folder,r"YOLODataset\labels\val")
        yaml_file = os.path.join(dataset_folder, r"YOLODataset\dataset.yaml")
        # os.remove(yaml_file)
        # shutil.copy("dataset.yaml", yaml_file)

        ### excessive class 3 -> 0 ###
        # names: ['0', '3', '1', 'boat'] in yaml file 

        # dest_folder = r"refined\train"
        os.makedirs(dest_folder_train, exist_ok=True)

        for filename in os.listdir(folder_train):
            filepath = os.path.join(folder_train, filename)
            dest_filepath = os.path.join(dest_folder_train, filename)
            with open (dest_filepath, "w") as fout:
                print ('written in', dest_filepath)
                dest_ls = []
                with open (filepath, "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        line_ls = line.split(' ')
                        if line_ls[0] in class_need_replace_ls:
                            new_line = class_replace_in + line[1:]
                            dest_ls.append(new_line)
                        else:
                            dest_ls.append(line)
                    for item in dest_ls:
                        fout.write(item)


        # dest_folder = r"refined\train"
        os.makedirs(dest_folder_val, exist_ok=True)

        for filename in os.listdir(folder_val):
            filepath = os.path.join(folder_val, filename)
            dest_filepath = os.path.join(dest_folder_val, filename)
            with open (dest_filepath, "w") as fout:
                print ('written in', dest_filepath)
                dest_ls = []
                with open (filepath, "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        line_ls = line.split(' ')
                        if line_ls[0] in class_need_replace_ls:
                            new_line = class_replace_in + line[1:]
                            dest_ls.append(new_line)
                        else:
                            dest_ls.append(line)
                    for item in dest_ls:
                        fout.write(item)

        if os.path.exists(folder_train):
            shutil.rmtree(folder_train)
        if os.path.exists(folder_val):
            shutil.rmtree(folder_val)
        shutil.copytree(dest_folder_train, folder_train)
        shutil.copytree(dest_folder_val, folder_val)

if __name__ == "__main__":
    main()