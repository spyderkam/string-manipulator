# <p align="center"> String Manipulation for Boeing </p>     <!--github version not HTML-->

The `Text` class takes in string data and gives out needed data.

## Methods

### Finding Strings

The `find_string` method returns a tuple of the number of times a word of interest appears in a text as well as the starting position of the first charachter of that word.

```
text = string_manipulator.Text(input_text)
finder = text.find_string
```

Here, applying `finder(word)[0]` will return the number of times `word` appears in the inputted string and `finder(word)[1]` will return the starting positions of the first charachter of `word` in input string. <br>

### Dividing Large Files Into $n$ Smaller Files

The `divide_by_lines` method of the `Text` class divides the input file into a desired amount of smaller files. It can make the output files into any desired extension.

```
with open("big.txt", "r") as f:
    all_file_lines = f.readlines()

all_file_lines = [lines.replace("\n", '') for lines in all_file_lines]
all_lines = Text(all_file_lines)
all_lines.divide_by_lines(No_lines=len(all_file_lines), divfiles=12, folder='nfiles', ext='dat')
```

`No_lines` is the number of lines in the input files and $n =$ `divfiles` is the number of files the input file will be divided into. The new files will be named `𝚤_file.extension` where `𝚤` starts from `0`. Each file will have an equal amount of lines in it *but* the <ins>last file</ins> created *might* be longer than its preceding files depending on `No_lines % divfiles`. <br>

### Splitting Large Files Into Files Containing a Maxed Out Number of Lines

To split a file into smaller file where each file has no more than a certain amount of lines in it use the `split_by_lines` method of the `Text` class. 

```
file = Text(inputFile)
file.split_by_lines(divlines, ext, folder)
```

`divlines` is the *maximum* number of lines in the newly created files, `ext` is the extension of the new files, and `folder` is the directory which they will be stored in. The last generated file might have less than `divlines` depending on the number of lines in the input file. The newly created files will be dubbed as `splittedFile_𝚤.ext` where `𝚤` starts from `0`. <br>

### Split Large Files Into Smaller Files by Size

To split files by the size of their size, call the `split_by_size` method. 

```
file = Text(input_file)
file.split_by_size(size, ext, folder, fname)
```
`size` is the size of the output files in bytes, `ext` is the extension of both the input and output files, and `folder` is the directory which the *output files* will be stored in. If `folder` does not exist then the program will create it. The new files will be named `fname_𝚤.ext` where `𝚤` starts from `0`. <br>

## Automatic Execution of Methods

If you wish to automatically have these methods applied, simply just execute one of the `run_method.py` scripts. Once any one of them has been ran, a series of questions will be prompted in the terminal's user interface and you can apply the respective method to one or multiple files in the directory or a subdirectory. <br>
&nbsp;&nbsp;&nbsp;&nbsp;`run_split_by_lines.py` and `run_divide_by_lines.py` are currently in development. Please ignore `run_all.py`.
