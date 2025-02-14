import os 
"""
count all class 
"""
folder = r"NAM_ALL_REFINED\YOLODataset\labels\train"
t = {}
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            cls = line.split(" ")[0]
            if cls not in t:
                t[cls] = 1
            else: 
                t[cls] += 1

folder = r"NAM_ALL_REFINED\YOLODataset\labels\val"

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            cls = line.split(" ")[0]
            if cls not in t:
                t[cls] = 1
            else: 
                t[cls] += 1
print (t)
