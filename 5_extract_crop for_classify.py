"""
from yolo txt extract crop image to make a classify dataset
"""
import os
import cv2
import uuid

SAVE_SHIP_FOLDER = "classify_dataset"

def coor2coor(x_center, 
              y_center, 
              width, 
              height, 
              imageWidth, 
              imageHeight):
    x_center = x_center * imageWidth
    y_center = y_center * imageHeight
    width = width * imageWidth
    height = height * imageHeight

    x_min = x_center - width / 2
    y_min = y_center - height / 2
    x_max = x_center + width / 2
    y_max = y_center + height / 2

    return [x_min, y_min, x_max, y_max]


import cv2

def save_detect_yolo(x_center, y_center, width, height, img_path, save_path_crop):
    img = cv2.imread(img_path)
    imageHeight, imageWidth, _ = img.shape
    coor = coor2coor(x_center, y_center, width, height, imageWidth, imageHeight)
    x_min, y_min, x_max, y_max = coor
    x_min, y_min, x_max, y_max = int(x_min), int(y_min), int(x_max), int(y_max)
    # Crop the image using array slicing
    cropped_img = img[y_min:y_max, x_min:x_max]
    
    # Save the cropped image
    cv2.imwrite(save_path_crop, cropped_img)



train_labels = r"YOLODataset\labels\train"
train_images = r"YOLODataset\images\train"
val_labels = r"YOLODataset\labels\val"
val_images = r"YOLODataset\images\val"
from tqdm import tqdm
for filename in tqdm(os.listdir(train_labels), total = len(os.listdir(train_labels))):
    label_file = os.path.join(train_labels, filename)
    image_file = os.path.join(train_images, filename.replace(".txt", ".png"))
    with open(label_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            line_ls = line.split(' ')
            class_crop = line_ls[0]
            os.makedirs(os.path.join(SAVE_SHIP_FOLDER, class_crop), exist_ok=True)
            x_center, y_center, width, height = line_ls[1:]
            x_center, y_center, width, height = float(x_center), float(y_center), float(width), float(height)
            save_path_crop = os.path.join(SAVE_SHIP_FOLDER, class_crop, str(uuid.uuid4()) + ".jpg")
            img_path = image_file
            save_detect_yolo(x_center, 
                            y_center, 
                            width, 
                            height,
                            img_path, 
                            save_path_crop)
for filename in tqdm(os.listdir(val_labels), total = len(os.listdir(val_labels))):
    label_file = os.path.join(val_labels, filename)
    image_file = os.path.join(val_images, filename.replace(".txt", ".png"))
    with open(label_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            line_ls = line.split(' ')
            class_crop = line_ls[0]
            os.makedirs(os.path.join(SAVE_SHIP_FOLDER, class_crop), exist_ok=True)
            x_center, y_center, width, height = line_ls[1:]
            x_center, y_center, width, height = float(x_center), float(y_center), float(width), float(height)
            save_path_crop = os.path.join(SAVE_SHIP_FOLDER, class_crop, str(uuid.uuid4()) + ".jpg")
            img_path = image_file
            save_detect_yolo(x_center, 
                            y_center, 
                            width, 
                            height,
                            img_path, 
                            save_path_crop)