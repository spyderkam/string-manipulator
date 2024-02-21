from string_manipulator import Text     # As of now string_manipulator only has Text class.


file = input("Enter the path to the file you are trying to split: ")
last_dot_index = file.rfind(".")

text = Text(file)

extension = file[last_dot_index+1::]
size = int(input("What is size of the new files you want (in bytes): "))

text.split_by_size(size, extension)
