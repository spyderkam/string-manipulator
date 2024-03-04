from glob import glob
from string_manipulator import Text



o_or_m = input(
    "Do you want to split multiple files with a specific extension or just one file? Enter 'o' for one or 'm' for multiple: ").lower()



if o_or_m == 'o':
    file = input("Enter the path to the file you are trying to split: ")
    n = int(input("Enter the number of new files you want the original file splitted into: "))

    last_dot_index = file.rfind(".")
    extension = file[last_dot_index+1::]

    with open(file, "r") as f:
        all_file_lines = f.readlines()
        
        all_file_lines = [lines.replace("\n", '') for lines in all_file_lines]
        all_lines = Text(all_file_lines)
        all_lines.divide_by_lines(No_lines=len(all_file_lines), divfiles=n, ext=extension, dir='nfiles')


elif o_or_m == 'm':
    extension = input("What is the extension of the files you want to split?: ")
    this_dir_yn = input(f"Are the {extension} files in the current directory? Enter 'y' for yes or 'n' for no: ")

    if this_dir_yn == 'n':
        which_dir = input(f"Enter the path to the directory which the {extension} files are in: ")
        files = sorted(glob(f"{which_dir}/*.{extension}"))
        if not files:
            raise ValueError(f"Something went wrong, no files with extension '{extension}' found in '{which_dir}' directory!")
    elif this_dir_yn == 'y':
        files = sorted(glob(f"*.{extension}"))
        if not files:
            raise ValueError(f"Something went wrong, no files with extension '{extension}' found in this directory!")
    else:
        raise ValueError("YOU MUST ENTER 'y' FOR YES OR 'n' FOR NO!")

    n = int(input("Enter the number of new files you want the original file splitted into: "))
    count = 0

    for file in files:
        with open(file, "r") as f:
            all_file_lines = f.readlines()
            
            all_file_lines = [lines.replace("\n", '') for lines in all_file_lines]
            all_lines = Text(all_file_lines)
            all_lines.divide_by_lines(len(all_file_lines), n, f'nfiles{count}', extension)

        count += 1
else:
    raise ValueError("YOU MUST ENTER 'o' FOR ONE OR 'm' FOR MULTIPLE!")

