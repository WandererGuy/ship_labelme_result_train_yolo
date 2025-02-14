@echo off
setlocal
set current_dir=%~dp0
set previous_dir=%~dp0..
set JSON_FOLDER_TO_CONVERT = "NAM_ALL_REFINED"
call conda activate "%previous_dir%\env"
python 0_prepare_all_dataset.py
python 1_labelme2yolo.py --json_dir %JSON_FOLDER_TO_CONVERT%
python 2_check_class.py
python 3_remove_label.py
python 4_train_yolo.py

