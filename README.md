from a folder result of labelme labelling (this folder can have subfolder or not) (have images and corresponding json)<br>
convert to yolo training dataset<br>
steps:
- convert json to yolo txt 
- replace unwanted class with wanted class 
- then train yolo with new yolo dataset 


## Preparation

1. **Configure the `config.yaml` file**:
   - Open the `config.yaml` file.
   - Set the correct value for `SOURCE_FOLDER` to point to your Labelme dataset (the folder containing images and corresponding JSON files).

2. **Run the conversion and preparation commands**:
   - Execute the commands in the provided `START.bat` file to convert the dataset and set up the YOLO dataset.

3. **YOLO Dataset Output**:
   - The resulting dataset will be stored in the `./YOLODataset` folder.

4. **Update the YOLO Configuration**:
   - Before training YOLO, modify the `./YOLODataset/dataset.yaml` file to match your YOLO training requirements (e.g., class names, paths).

## Training YOLO

- After the conversion is done, use your preferred YOLO training method with the prepared dataset located in the `./YOLODataset` folder.
make your own dataset.yaml , i have one example in dataset.yaml
```
python 5_train_yolo.py
```

---


