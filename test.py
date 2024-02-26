from string_manipulator import Text

inputFilePath = "inputs/120.txt"
file = Text(inputFilePath)

file.split_by_lines(2, "txt", "output")
