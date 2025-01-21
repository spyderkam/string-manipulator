#!/usr/bin/env python3

from xlsxwriter.utility import xl_col_to_name

__author__ = "spyderkam"

def getLetters(headers, dataFrame: 'pandas.core.frame.DataFrame') -> dict:
    """Get Excel column letters for given header names."""
    letters = {}
    for header in headers:
        column_number = dataFrame.columns.get_loc(header) 
        letters[header] = xl_col_to_name(column_number)
    return letters

def getHeaders(letters, dataFrame: 'pandas.core.frame.DataFrame') -> dict:
    """Get header names for given Excel column letters."""
    HEADERS = list(dataFrame.columns)
    headers = {}
    for letter in letters:
        column_number = colLetter_to_Num(letter)
        if column_number < len(HEADERS):
            headers[letter] = HEADERS[column_number]
    return headers

def colLetter_to_Num(letter: str) -> int:
    """Convert Excel column letter to number (A=0, B=1, etc.)"""
    return sum((ord(char) - ord('A') + 1) * (26 ** i) for i, char in enumerate(reversed(letter))) - 1

def colHeader_to_Letter(requiredColumns: list, dataFrame: 'pandas.core.frame.DataFrame') -> str:
    """Returns a string of column letters for given header names."""
    requiredColumnLetters = ""
    for i, columnLetter in enumerate((misc.getLetters(column, dataFrame=dataFrame) for column in requiredColumns)):
        columnLetter = list(columnLetter.values())[0]     # should just be one value anyway
        if i == len(requiredColumns) - 1:
            requiredColumnLetters += columnLetter
        else:
            requiredColumnLetters += columnLetter + ", "
    return requiredColumnLetters

def stringOfLettersList(headers: list, dataFrame: 'pandas.core.frame.DataFrame') -> str:
    """Return a string type of a list of letters; e.g., 'A, B, C'"""
    letters = list(getLetters(headers, dataFrame).values())
    requiredColumnLetters = ""
    for i, columnLetter in enumerate(letters):
        if i == len(letters) - 1:
            requiredColumnLetters += columnLetter
        else:
            requiredColumnLetters += columnLetter + f"{columnLetter}, "
    return requiredColumnLetters


if __name__ == "__main__":
    import pandas as pd
    
