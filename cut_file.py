# May and probably will fail certain test cases.

class File:
    """Text class for input file."""

    def __init__(self, file_lines):
        self.file_lines = file_lines

    def create_smaller_files(self, NO_lines, divlines):     # NO_lines = number of lines in original file; divlines ≈ how many lines in divided files
        """something"""

        ogfl = self.file_lines     # original file lines
        remainder = NO_lines % divlines

        #foo = NO_lines - remainder
        mnlef = int( (NO_lines - remainder)/divlines )     # (m)ax (N)o of (l)ines in (e)ach (f)ile

        if remainder != 0:
            # NO_new_files will be a list containing the number of files (0 and so on)
            NO_new_files = divlines + 1
        else:
            NO_new_files = divlines



        for i in range(NO_new_files):
            new_file = open(f"new_files/{i}_file.txt", "w")

            if i + 1 != NO_new_files:
                a = ogfl[i*mnlef:(i+1)*mnlef]
                for line in a:
                    line = str(line)
                    #a = a.replace("[", "").replace("]", "")
                    new_file.writelines(line[1:-2] + "\n")
            
            else:
                b = ogfl[i*mnlef::]
                for line in b:
                    line = str(line)
                    #b = b.replace("[", "").replace("]", "")
                    new_file.writelines(line[1:-2] + "\n")
