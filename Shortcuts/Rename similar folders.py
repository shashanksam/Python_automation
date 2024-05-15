import os
import re


def rename_folders(path):

    NAMES = [
        "Sorting",
        "Function - NVL",
        "Group By Having",
        "Inner Join and Group By Having",
        "3 levels of Left Outer Join, NVL, Group By",
        "Self Join and inner join",
    ]
    dir_list = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    pos = 0
    for folder in dir_list:
        match = re.match(r"New folder(.+)", folder)
        if match:
            new_folder_name = NAMES[pos]
            pos += 1
            src = os.path.join(path, folder)
            dst = os.path.join(path, new_folder_name)
            os.rename(src, dst)
            print(f"Renamed folder '{src}' to '{dst}'")


project_path = "C:\Ta\Training\Day 2"
rename_folders(project_path)
