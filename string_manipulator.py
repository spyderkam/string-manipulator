import numpy as np
import os
import pandas as pd
import re
import subprocess



class Text:
    """Text class for input file."""

    def __init__(self, content):
        self.content = content


    def find_string(self, substring):
        """Finding a substring; how many times it appears and in what positions."""

        TEXT = self.content     # Placeholder so that self.content would not be modified.
        index_list = [term.start() for term in re.finditer(substring, TEXT)]

        return len(index_list), index_list


    def divide_by_lines(self, No_lines, divfiles, folder, ext):     # No_lines = # of lines in inFile; divfiles = # of new files; folder = output dir; ext = outFile type
        """Divide larger file into a divfiles number of files."""
        # Efficient or not?

        ogfl = self.content     # original file lines
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

        ogf = self.content     # original file path
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

        ogf = self.content     # original file path
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
            outFile.close()



class ExSpread:
    """Spreadsheet related manipulation."""

    def __init__(self, fpath: str, search=None):
        self.fpath = fpath
        self.search = search     # optional parameter to be searched


    def mk_timesheet(self, folder: str, fname: str):  # folder = outFile dir; fname = outFile name
        """Making xlsx/CSV(?) file with timestamps"""

        ogf = self.fpath     # original file path
        s = self.search      # string to be searched

        if not os.path.isdir(folder):
            subprocess.call(f"mkdir {folder}", shell=True)

        rows = []         
        with open(ogf, "r", encoding="utf8") as f:
            temp_lines = f.readlines()
            for lineNo_m1, line in enumerate(temp_lines):     # lineNo_m1 = 'line number' - 1
                if line.strip() == s:
                    count = 1
                    while temp_lines[lineNo_m1+count][0] == " " and temp_lines[lineNo_m1+count][1].isdigit():
                        rows.append(temp_lines[lineNo_m1+count].strip().split())
                        count += 1

        arr = np.zeros((len(rows),len(max(rows, key=lambda x: len(x)))), dtype='<U11')
        arr[:] = " "     # compare with np.nan

        for 𝚤,𝚥 in enumerate(rows):
            arr[𝚤][0:len(𝚥)] = 𝚥
        arr = np.transpose(arr)

        df = pd.DataFrame({'year': arr[0], 'month': arr[1], 'day': arr[2], 'hour': arr[3],
                           'minute': arr[4], 'second': arr[5], 'time_zone': arr[6]})
        df.to_csv(f"{folder}/{fname}.CSV", index=False)  # df.to_csv vs df.to_excel




if __name__ == "__main__":
    """Testing"""

    input_file = ExSpread("sample_inputs/sample.ascii_out", "K11_3_1_HEARTBEAT_MO.INSTANCΕ")
    input_file.mk_timesheet(os.getcwd(), "outFile")
