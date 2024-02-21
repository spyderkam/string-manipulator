# String Manipulation for Boeing

The `Text` class takes in string data and gives out needed data.

## Methods

### Finding Strings

The `find_word` method returns a tuple of the number of times a word of interest appears in a text as well as the starting position of the first charachter of that word.

```
text = string_manipulator.Text(input_text)
finder = text.find_word
```

Here, applying `finder(word)[0]` will return the number of times `word` appears in the inputted string and `finder(word)[1]` will return the starting positions of the first charachter of `word` in input string. <br>

### Dividing Large Files Into Smaller Files by Line Division

The `split_by_lines` method of the `Text` class divides the input file into a desired amount of smaller files. It can make the output files into any desired extension.

```
with open("big.txt", "r") as f:
    all_file_lines = f.readlines()

all_file_lines = [lines.replace("\n", '') for lines in file_lines]
all_lines = string_manipulator.Text(file_lines)
all_lines.split_by_lines(No_lines=len(file_lines), divfiles=12, extension='dat')
```

`No_lines` is the number of lines in the input files and `divfiles` is the number of files the input file will be divided into. The file could potential be divided into one more than `divfiles` depending on the number of lines in the input file. The new files will be named `𝚤_file.extension` where `𝚤` starts from `0`. <br>
<null>
&nbsp;&nbsp;&nbsp;&nbsp;To start, please make sure a directory named `less_line_files` is in the directory which `string_manipulator` is executed. <br>

### Dividing Large Files Into Smaller Files by Size

To split files by the size of their size, call the `split_by_size` method. 

```
file = Text(input_file)
file.split_by_size(size, ext, dir)
```
`size` is the size of the output files in bytes, `ext` is the extension of both the input and output files, and `dir` is the directory which the *output files* will be stored in. If `dir` does not exist then the program will create it. <br>

## Automatic Execution of Methods
