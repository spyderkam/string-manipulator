from glob import glob
from pathlib import Path
import re
from string_manipulator import ExSpread
import os


o_or_m = input("Do you want to make timesheets for multiple files or just one file? Enter 'o' for one or 'm' for multiple: ").lower()


if o_or_m == 'o':
    file_path = input("Enter the path to the file: ")
    srch = input("Enter the message string to be searched: ")

    input_file = ExSpread(fpath=file_path, search=srch)
    alt_dir_yn = input("Do you want to store the new files in an alternative directory? Enter 'y' for yes or 'n' for no: ").lower()

    if alt_dir_yn == 'n':
        dirName = os.path.abspath(os.path.dirname(file_path))

        s_lst = re.split('[^a-zA-Z]', srch)
        s_lst2 = []
        for term in s_lst:
            if len(term) >= 4:
                s_lst2.append(term)
        ss = ('_').join(s_lst2)

        input_file.mk_timesheet(dirName, ss)




# This is from run_split_by_size.py
"""
    elif alt_dir_yn == 'y':
        alt_dir = input("Enter the path to the alternative directory: ")
        text.split_by_size(size, extension, alt_dir, fileName)
    else:
        raise ValueError("YOU MUST ENTER 'y' FOR YES OR 'n' FOR NO!")




elif o_or_m == 'm':
    extension = input("Enter the type of the files you want to split: ").lower()
    this_dir_yn = input(f"Are the {extension} type files in the current directory? Enter 'y' for yes or 'n' for no: ").lower()

    if this_dir_yn == 'n':
        which_dir = input(f"Enter the path to the directory which the {extension} type files are in: ")
        files = sorted(glob(f"{which_dir}/*.{extension}"))
        if not files: raise ValueError(f"Something went wrong, no files with type '{extension}' found in '{which_dir}' directory!")
    elif this_dir_yn == 'y':
        which_dir = Path(__file__).parent.resolve()
        files = sorted(glob(f"*.{extension}"))
        if not files: raise ValueError(f"Something went wrong, no files with type '{extension}' found in this directory!")
    else:
        raise ValueError("YOU MUST ENTER 'y' FOR YES OR 'n' FOR NO!")

    size = int(input("What is size of the new files you want (in bytes)? "))
    count = 0
    alt_dir_yn = input("Do you want to store the new files in an alternative directory? Enter 'y' for yes or 'n' for no: ").lower()

    if alt_dir_yn == 'n':
        for file in files:
            fileName = Path(file).stem
            text = Text(file)
            text.split_by_size(size, extension, which_dir, fileName)

            count += 1
    elif alt_dir_yn == 'y':
        multi_dir_yn = input("Do you want each set of splitted files to be in a seperate directory? Enter 'y' for yes or 'n' for no: ").lower()
        if multi_dir_yn == 'n':
            alt_dir = input("Enter the path to the singular alternative directory: ")
            for file in files:
                fileName = Path(file).stem
                text = Text(file)
                text.split_by_size(size, extension, f"{alt_dir}", fileName)

                count += 1
        elif multi_dir_yn == 'y':
            alt_dir = input("Enter one path to the muiltiple alternative directories and they will be generated distinctively by count: ")
            for file in files:
                fileName = Path(file).stem
                text = Text(file)
                text.split_by_size(size, extension, f"{alt_dir}_{count}", fileName)

                count += 1
        else:
            raise ValueError("YOU MUST ENTER 'y' FOR YES OR 'n' FOR NO!")
    else:
        raise ValueError("YOU MUST ENTER 'y' FOR YES OR 'n' FOR NO!")



else:
    raise ValueError("YOU MUST ENTER 'o' FOR ONE OR 'm' FOR MULTIPLE!")
"""
