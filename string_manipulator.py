# May and probably will fail certain test cases. Could give it a better name, maybe not?

class Text:
    """Text class for input file."""

    def __init__(self, text):
        self.text = text


    def find_word(self, word):
        """Finding a specific word in the input text; how many times it appears and in what positions."""

        if word != word.lower():
            raise ValueError("Enter word in all lowercase.")     # This method can definetly be upgraded.

        TEXT = self.text     # Using a variable placeholder for self.text so that self.text would not be modified.
        index_list = []
        word_in_text = True

        while word_in_text:
            i = (TEXT).find(word)
            if i != -1:
                index_list.append(i)

                TEXT = [*TEXT]           # Convert string to list of charachters.
                TEXT[i] = "A"            # Placeholder letter, must be capital in this implementation.
                TEXT = ''.join(TEXT)     # Convert back to string.

            else:
                break
        return len(index_list), index_list


    def create_smaller_files(self, NO_lines, divfiles, extension='txt'):     # NO_lines = number of lines in original file; divfiles ≈ how many lines in divided files
        """Divide larger file into a divfiles number of files potentially + 1."""

        ogfl = self.text     # original file lines
        remainder = NO_lines % divfiles
        mnlef = int( (NO_lines - remainder)/divfiles )     # (m)ax (N)o of (l)ines in (e)ach (f)ile; Always an integer but data type needs to be int for indexing.

        if remainder != 0:
            # NO_new_files will be a list containing the number of files (0 and so on)
            NO_new_files = divfiles + 1
        else:
            NO_new_files = divfiles

        # When in Unix can use subprocess to create smaller_files directory here.
        for i in range(NO_new_files):
            new_file = open(f"smaller_files/{i}_file.{extension}", "w")

            if i + 1 != NO_new_files:
                lines_to_write = ogfl[i*mnlef:(i+1)*mnlef]
                for line in lines_to_write:
                    line = str(line)
                    new_file.writelines(line[1:-2] + "\n")     # 1 to -2 in order to eliminate printed quote symbols

            else:
                lines_to_write = ogfl[i*mnlef::]                            # in case number of lines is less than mnlef
                for line in lines_to_write:
                    line = str(line)
                    new_file.writelines(line[1:-2] + "\n")



if __name__ == '__main__':
    # https://www.askpython.com/python/examples/read-file-as-string-in-python
    with open("inputs/16_missile.txt", "r") as f:
        data = f.read().lower()

    text = Text(data)
    print(text.find_word('missile'))


    with open("inputs/big.txt", "r") as f:
        file_lines = f.readlines()

    file_lines = [lines.replace("\n", '') for lines in file_lines]
    lines = Text(file_lines)
    lines.create_smaller_files(NO_lines=len(file_lines), divfiles=12)     # Could potentially have one more than divfile based on remainder.
