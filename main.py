# https://unix.stackexchange.com/questions/101332/generate-file-of-a-certain-size

#import os
#print(os.path.getsize("inputs/big.txt"))

from string_manipulator import *

with open("inputs/big.txt", "r") as f:
    file_lines = f.readlines()

file_lines = [lines.replace("\n", '') for lines in file_lines]
#print(file_lines)
lines = Text(file_lines)
lines.create_smaller_files(NO_lines=len(file_lines), divlines=12, extension='dat')    # could potentially have one more than divline based on remainder


with open("inputs/16_missile.txt", "r") as f:
    data = f.read().lower()

text = Text(data)
finder = text.find_word
print(f"The words missile appears {finder('missile')[0]} times in the file 16_missile.txt at positions {finder('missile')[1]}.")
