from string_manipulator import *     # As of now * is only Text class.


file_path1 = "inputs/missile16.fort13" 
with open(file_path1, "r") as f:
    data = f.read().lower()

text = Text(data)
finder = text.find_word
print(f"The words missile appears {finder('missile')[0]} times in the file 16_missile.txt at positions {finder('missile')[1]}.")


file_path2 = "inputs/big.txt"
with open(file_path2, "r") as f:
    all_file_lines = f.readlines()

all_file_lines = [lines.replace("\n", '') for lines in file_lines]
# print(all_file_lines)
all_lines = Text(all_file_lines)
# could potentially have one more than divline based on remainder
all_lines.split_by_lines(NO_lines=len(file_lines), divfiles=11, extension='dat')
