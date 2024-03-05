from glob import glob
from string_manipulator import Text


word = input("What is the string you want to find? ")
o_or_m = input(f"Do you want to find the string '{word}' in just one file or multiple files that are splitted from one file? Enter 'o' for one or 'm' for multiple: ")


if o_or_m == 'o':
    file_path = input("Enter the path to the file of interest: ")
    with open(file_path, "r") as f:
        datum = f.read()

    text = Text(datum)
    finder = text.find_string
    
    pos_out_yn = input(f"Do you want to output each position of the first charachter of the substring {word} in the string? Enter 'y' for yes or 'n' for no: ").lower()
    if pos_out_yn == 'y':
        print(f"The string '{word}' appears '{finder(word)[0]}' times in '{file_path}' at positions '{finder(word)[1]}'.")
    elif pos_out_yn == 'n':
        print(f"The string '{word}' appears '{finder(word)[0]}' times in '{file_path}'.")
    else:
        raise ValueError("YOU MUST ENTER 'y' FOR YES OR 'n' FOR NO!")

elif o_or_m == 'm':
    ext = input("Enter the type of the files: ").lower()
    fname = input(f"Enter the name of the files in which you want find the substring `{word}` in WITHOUT entering the underscore, number, or type that follows them: ")
    this_dir_yn = input("Are the files in the current directory? Enter 'y' for yes or 'n' for no: ").lower()

    if this_dir_yn == 'n':
        which_dir = input("Enter the path to the directory which the files are in: ")
        files = sorted(glob(f"{which_dir}/{fname}_*.{ext}"))     # Not sure of it needs to be sorted but it can't hurt...
        if len(files) == 0: raise ValueError(f"Something went wrong, no '{ext}' type files found in '{which_dir}' directory!")
    elif this_dir_yn == 'y':
        files = sorted(glob(f"{fname}_*.{ext}"))                 # Not sure of it needs to be sorted but it can't hurt...
        if len(files) == 0: raise ValueError(f"Something went wrong, no '{ext}' type files found in this directory!")
    else:
        raise ValueError("YOU MUST ENTER 'y' FOR YES OR 'n' FOR NO!")

    texts = []
    No_times = []      # List of number of times the word appears in each file.
    # indexes = []     # List of the first index of the word in each file (list of lists).
        
    for file in files:
        with open(file, "r") as f:
            datum = f.read()
        texts.append( Text(datum) )
    
    for text in texts:
        No_times.append( text.find_string(word)[0] )
        #indexes.append( text.find_string(word)[1] )

    print(f"The number of times '{word}' appears in these files is '{sum(No_times)}'.")     # Currently no index output applied here...
else:
    raise ValueError("YOU MUST ENTER 'o' FOR ONE OR 'm' FOR MULTIPLE!")
