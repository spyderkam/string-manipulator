#!/usr/bin/env python3.12

__author__ = "Kamyar Modjtahedzadeh"

import h5py
import numpy as np


# Ignore path for now. Just assume that all the working files are always in a subdirectory called 'files.'
# Source for work: https://pythonforthelab.com/blog/how-to-use-hdf5-files-in-python/.

class HDF5:
    """Class of HDF5 files."""

    def __init__(self, filename):
        self.filename = filename     # So this would be "FTX-26_DEL LRDR-PRE-002E LRDR Sensor Data_TC1.h5"


    def findVar(self, var_x):        # find variable
        """Returns a dictionary whose keys are the keys which contain the variable and the values
        are lists containing the indices of that variable in the respective HDF5 key."""        

        h5_varNames, varNames = self.genSets()[1], self.genSets()[2]
        if var_x not in varNames:
            raise ValueError(f"Variable '{var_x}' does not exist.")

        outSet = {}
        for key, value in h5_varNames.items():
            found = len(np.where(value == var_x)[0])  # = 0 if not found. Extra line added for clarity.
            if found:
                outSet[key] = [i for i in np.where(value == var_x)[0]]
        return outSet
    

    def genSets(self):     # gererate sets
        """Generating HDF5 full set, HDF5 set of units, and flat array
        of all the units; i.e., h5_dict, h5_varNames, and varNames."""

        h5_dict, h5_varNames = {}, {}
        with h5py.FILE(f"files/{filename}", "r") as f:
            #print("\033[4mKeys From Imported HDF5 File\033[0m")
            for key in f.keys():
                #print(key)
                h5_dict[key] = f[key][()]                              # HDF5 full set. 
                h5_varNames[key] = np.array(h5_dict[key].dtype.names)  # HDF5 set w/usual keys and unit arrays as values.

            varNames = np.array([])                                    # Flat array of all the units.
            for key, variables in h5_varNames.items():
                varNames = np.append(varNames, variables)
        return h5_dict, h5_varNames, varNames



if __name__ == '__main__':
    '''Note that half of this sample—i.e., the txtFiles part—is strictly related to in lab stuff.
    So there is no point in analyzing it outside of the lab.'''
    
    from glob import glob

    filename = "FTX-26_DEL LRDR-PRE-002E LRDR Sensor Data_TC1.h5"
    txtFiles = sorted(glob("files/*BmdsLog1.txt"))

    fileHeaders = []     # Headers of the .txt files.
    for file in txtFiles:
        with open(file, "r") as f:
            fileHeaders.append(f.readline()[:-2].split("\t"))
    all_fileHeaders = sorted(list(set([header for headers_lst in fileHeaders for header in headers_lst])))
    # https://stackoverflow.com/a/952952/14379288

    h5_file = HDF5(filename)
    #print(f"The variable 'Time' is found in the following HDF5 keys: {h5_file.finVar('Time')}")
    h5_dict, h5_varNames, varNames = h5_file.genSets()[0], h5_file.genSets()[1], sorted(list(set(h5_file.genSets()[2])))
    # Note that the reasoning begind sorted(list(set(data))) should be obvious.

    #print(h5_dict["ArrayBias.out"].dtype)
    hdf5_headers = list(h5_varNames.keys())     # or list(h5_dict.keys())       
