# https://unix.stackexchange.com/questions/101332/generate-file-of-a-certain-size

#import os
#print(os.path.getsize("inputs/big.txt"))

from string_manipulator import *

file_path1 = "inputs/big.txt"
with open(file_path1, "r") as f:
    file_lines = f.readlines()

file_lines = [lines.replace("\n", '') for lines in file_lines]
#print(file_lines)
lines = Text(file_lines)
lines.create_smaller_files(NO_lines=len(file_lines), divfiles=12, extension='dat')    # could potentially have one more than divline based on remainder


file_path2 = "inputs/16_missile.txt"
with open(file_path2, "r") as f:
    data = f.read().lower()

text = Text(data)
finder = text.find_word
print(f"The words missile appears {finder('missile')[0]} times in the file 16_missile.txt at positions {finder('missile')[1]}.")
