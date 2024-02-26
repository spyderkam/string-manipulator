import os
import subprocess


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



    def divide_by_lines(self, No_lines, divfiles, dir, ext):     # No_lines = # of lines in OG file; divfiles = # of new files; ext = extension of output file
        """Divide larger file into a divfiles number of files."""

        ogfl = self.text     # original file lines
        remainder = No_lines % divfiles
        mnlef = int( (No_lines - remainder)/divfiles )     # (m)ax (N)o of (l)ines in (e)ach (f)ile; Always an integer but data type needs to be int for indexing.

        subprocess.call(f"mkdir {dir}", shell=True)     # Must use shell=True otherwise doesn't work on Windows.

        for i in range(divfiles):     # *****
            new_file = open(f"{dir}/{i}_file.{ext}", "w")

            if i + 1 != divfiles:     # *****
                lines_to_write = ogfl[i*mnlef:(i+1)*mnlef]
                for line in lines_to_write:
                    line = str(line)
                    new_file.writelines(line + "\n")     # 1 to -2 in order to eliminate printed quote symbols

            else:
                lines_to_write = ogfl[i*mnlef::]               # in case number of lines is less than mnlef
                for line in lines_to_write:
                    line = str(line)
                    new_file.writelines(line + "\n")
            new_file.close()



    def split_by_lines(self, divlines, ext, dir):     # divlines = max lines in divided files; ext = output extension, dir = directory to store put output files
        """Split input file into output files that have divlines number of lines in them."""
        # inefficient

        ogf = self.text     # original file
        subprocess.call(f"mkdir {dir}", shell=True)     # Must use shell=True otherwise doesn't work on Windows.

        file_number = 0
        f = open(ogf, "r")
        g = f.read()

        while True:
            if not g: break
            outFile = open(f"{dir}/splittedFile_{file_number}.{ext}", "w")

            for i in range(divlines):
                x = g.find('\n')
                h = g[0:x]
                outFile.write(h + "\n")
                g = g.lstrip(h).lstrip()
            outFile.close()

            file_number = file_number + 1
        f.close()



    def split_by_size(self, size, ext, dir, fname):     # size = size of the new files in bytes; ext = output file extension; dir = directory to store put output files
        """Divide larger file into smaller files based on size."""
        # ABSTRACT: https://stackoverflow.com/questions/8096614/split-large-files-using-python/8096846#8096846

        ogf = self.text     # original file
        file_number = 0

        if not os.path.isdir(dir):
            subprocess.call(f"mkdir {dir}", shell=True)     # Must use shell=True otherwise doesn't work on Windows.

        with open(ogf, "r") as f:
            while True:
                temp_lines = f.readlines(size)
                if not temp_lines: break

                outFile = open(f"{dir}/{fname}_%d.{ext}" % file_number, "w")

                for line in temp_lines:
                    outFile.write(line)
                outFile.close()

                file_number += 1




if __name__ == '__main__':
    # https://www.askpython.com/python/examples/read-file-as-string-in-python
    with open("inputs/missile16.fort13", "r") as f:
        data = f.read().lower()

    text = Text(data)
    print(text.find_word('missile'))


    with open("inputs/big.txt", "r") as f:
        file_lines = f.readlines()

    file_lines = [lines.replace("\n", '') for lines in file_lines]
    lines = Text(file_lines)
    lines.divide_by_lines(No_lines=len(file_lines), divfiles=12, ext='txt', dir='divfiles')     # Could potentially have one more than divfile based on remainder. (divfiles=11 vs 12)
