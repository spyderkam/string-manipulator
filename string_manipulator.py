import os
import re
import subprocess


class Text:
    """Text class for input file."""

    def __init__(self, object):
        self.object = object



    def find_string(self, substring):
        """Finding a substring; how many times it appears and in what positions."""

        TEXT = self.object     # Placeholder so that self.object would not be modified.
        index_list = [term.start() for term in re.finditer(substring, TEXT)]

        return len(index_list), index_list



    def divide_by_lines(self, No_lines, divfiles, folder, ext):     # No_lines = # of lines in inFile; divfiles = # of new files; folder = output dir; ext = outFile type
        """Divide larger file into a divfiles number of files."""
        # Efficient or not?

        ogfl = self.object     # original file lines
        remainder = No_lines % divfiles
        mnlef = int((No_lines - remainder)/divfiles)     # (m)ax (N)o of (l)ines in (e)ach (f)ile; data type must be int for indexing.

        subprocess.call(f"mkdir {folder}", shell=True)   # Must use shell=True otherwise won't work on Windows(?)

        for i in range(divfiles): 
            new_file = open(f"{folder}/{i}_file.{ext}", "w")

            if i + 1 != divfiles:
                lines_to_write = ogfl[i*mnlef:(i+1)*mnlef]

                for line in lines_to_write:
                    line = str(line)
                    new_file.writelines(line + "\n")    
            else:
                lines_to_write = ogfl[i*mnlef::]     # Put all remaining lines in the last outFile.

                for line in lines_to_write:
                    line = str(line)
                    new_file.writelines(line + "\n")
            new_file.close()



    def split_by_lines(self, divlines, ext, folder):     # divlines = max No lines in outFiles; ext = output type, folder = directory to store put outFiles
        """Split input file into output files that have maximum divlines number of lines in them."""
        # inefficient

        ogf = self.object     # original file
        subprocess.call(f"mkdir {folder}", shell=True)   # Must use shell=True otherwise won't work on Windows(?)

        file_number = 0
        inFile = open(ogf, "r")
        lines_to_write = inFile.read()

        while lines_to_write:
            outFile = open(f"{folder}/splittedFile_{file_number}.{ext}", "w")

            for i in range(divlines):
                x = lines_to_write.find('\n')
                y = lines_to_write[0:x]
                outFile.write(y + '\n')
                lines_to_write = lines_to_write.lstrip(y).lstrip()
            outFile.close()

            file_number += 1
        inFile.close()



    def split_by_size(self, size, ext, folder, fname):     # size = outFile size (bytes); ext = outFile type; folder = dir to store outFile; fname = outFile name
        """Divide larger file into smaller files based on size."""
        # ABSTRACT: https://stackoverflow.com/questions/8096614/split-large-files-using-python/8096846#8096846

        ogf = self.object     # original file path
        file_number = 0

        if not os.path.isdir(folder):
            subprocess.call(f"mkdir {folder}", shell=True)     # Must use shell=True otherwise won't work on Windows(?)

        with open(ogf, "r") as f:
            while True:
                temp_lines = f.readlines(size)
                if not temp_lines: break

                outFile = open(f"{folder}/{fname}_%d.{ext}" % file_number, "w")

                for line in temp_lines:
                    outFile.write(line)
                outFile.close()

                file_number += 1




if __name__ == '__main__':
    # https://www.askpython.com/python/examples/read-file-as-string-in-python
    with open("inputs/missile16.fort13", "r") as f:
        data = f.read().lower()

    text = Text(data)
    print(text.find_string('missile'))


    with open("inputs/big.txt", "r") as f:
        file_lines = f.readlines()

    file_lines = [lines.replace("\n", '') for lines in file_lines]
    lines = Text(file_lines)
    lines.divide_by_lines(No_lines=len(file_lines), divfiles=12, ext='txt', folder='divfiles')
