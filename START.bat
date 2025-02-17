@echo off
setlocal
set current_dir=%~dp0
@REM set JSON_FOLDER_TO_CONVERT same as in config.yaml
call conda activate "%current_dir%env"
python 0_prepare_all_dataset.py
python 1_labelme2yolo.py --json_dir NAM_ALL_REFINED
python 2_check_class.py
python 3_replace_label.py
python 2_check_class.py
python 4_move_files.py
@REM python 5_train_yolo.py

