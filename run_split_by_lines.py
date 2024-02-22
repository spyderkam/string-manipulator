from string_manipulator import Text

inputFilePath = "inputs/big.txt"
file = Text(inputFilePath)

file.split_by_lines(1000, "txt", "output")
