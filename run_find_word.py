from glob import glob
from numpy import sum
from string_manipulator import Text     # As of now string_manipulator only has Text class.


word = input(f"What is the word you want to find? ").lower()
o_or_m = input(f"Do you want to find the word '{word}' in just one file or multiple files with a specific extension? Enter 'o' for one or 'm' for multiple: ")


if o_or_m == 'o':
    file_path = input("Enter the path to the file of interest: ")
    with open(file_path, "r") as f:
        datum = f.read().lower()

    text = Text(datum)
    finder = text.find_word
    
    print(f"The word '{word}' appears '{finder(word)[0]}' times in '{file_path}' at positions '{finder(word)[1]}'.")
elif o_or_m == 'm':
    ext = input("Type the extension of the files: ")
    this_dir_yn = input("Are the files in the current directory? Enter 'y' for yes or 'n' for no: ")

    texts = []
    No_times = []      # list of number of times the word appears in each file
    # indexes = []     # list of the first index of the word in each file (list of lists)
    
    if this_dir_yn == 'n':
        which_dir = input("Enter the path to the directory which the files are in: ")
        files = sorted(glob(f"{which_dir}/*.{ext}"))     # Not sure of it needs to be sorted but it can't hurt...
        if len(files) == 0: raise ValueError(f"Something went wrong, no files with extension '{ext}' found in '{which_dir}' directory!")
    elif this_dir_yn == 'y':
        files = sorted(glob(f"*.{ext}"))                 # Not sure of it needs to be sorted but it can't hurt...
        if len(files) == 0: raise ValueError(f"Something went wrong, no files with extension '{ext}' found in this directory!")    
    else:
        raise ValueError("YOU MUST ENTER 'y' FOR YES OR 'n' FOR NO!")
        
    for file in files:
        with open(file, "r") as f:
            datum = f.read().lower()
        texts.append( Text(datum) )
    
    for text in texts:
        No_times.append( text.find_word(word)[0] )
        #indexes.append( text.find_word(word)[1] )

    print(f"The number of times '{word}' appears in these files is '{sum(No_times)}'.")     # Currently no index output applied here...
else:
    raise ValueError("YOU MUST ENTER 'o' FOR ONE OR 'm' FOR MULTIPLE!")
