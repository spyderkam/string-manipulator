# String Manipulation for Boeing

The `Text` class takes in string data and gives out needed data.

## Finding Strings
The `find_word` method returns a tuple of the number of times a word of interest appears in a text as well as the starting position of the first charachter of that word.

```
text = Text(input_text)
finder = text.find_word
```

Here, applying `finder(word)[0]` will return the number of times `word` appears in `input_text` and `finder(word)[1]` will return the starting positions of the first charachter of `word` in `input_text`. <br>

## Dividing Large Files Into Smaller Files
The `create_smaller_files` method of the `Text` class divides the input file into a desired amount of smaller files potentially plus one depending on the input file. It can make the output files into any desired extension.

```
with open("big.txt", "r") as f:
    file_lines = f.readlines()

file_lines = [lines.replace("\n", '') for lines in file_lines]
lines = Text(file_lines)
lines.create_smaller_files(NO_lines=len(file_lines), divlines=12, extension='dat')
```
