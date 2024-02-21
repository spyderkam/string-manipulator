from glob import glob
from string_manipulator import Text


o_or_m = input("Do you want to split multiple files with a specific extension or just one file? Enter 'o' for one or 'm' for multiple: ").lower()


if o_or_m == 'o':
    file = input("Enter the path to the file you are trying to split: ")
    size = int(input("What is size of the new files you want (in bytes): "))

    last_dot_index = file.rfind(".")
    extension = file[last_dot_index+1::]
    text = Text(file)

    text.split_by_size(size, extension, "smaller_size_files")
elif o_or_m == 'm':
    extension = input("What is the extension of the files you want to split?: ")
    this_dir_yn = input(f"Are the {extension} files in the current directory? Enter 'y' for yes or 'n' for no: ")

    if this_dir_yn == 'n':
        which_dir = input(f"Enter the path to the directory which the {extension} files are in: ")
        files = sorted(glob(f"{which_dir}/*.{extension}"))
        if not files: raise ValueError(f"Something went wrong, no files with extension '{extension}' found in '{which_dir}' directory!")
    elif this_dir_yn == 'y':
        files = sorted(glob(f"*.{extension}"))
        if not files: raise ValueError(f"Something went wrong, no files with extension '{extension}' found in this directory!")
    else:
        raise ValueError("YOU MUST ENTER 'y' FOR YES OR 'n' FOR NO!")

    size = int(input("What is size of the new files you want (in bytes): "))
    count = 0
    for file in files:
        text = Text(file)
        text.split_by_size(size, extension, f"smaller_size_files{count}")

        count += 1
else:
    raise ValueError("YOU MUST ENTER 'o' FOR ONE OR 'm' FOR MULTIPLE!")
