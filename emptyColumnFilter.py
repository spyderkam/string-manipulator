__author__ = "Kamyar Modjtahedzadeh"

import pandas as pd

ms = "Master_1_052024_GOLDEN_RUNS.xlsx"      # ms = (M)aster (S)preadsheet 
df = pd.read_excel(ms, sheet_name="Main Sheet", skiprows=0)
df.fillna(value="NULL_VALUE", inplace=True)  # Filling in the nan values of df for set conversion.
headers = df.columns                         # Master Spreadsheet headers
#m = len(df[headers[0]]); n = len(headers)   # df is an m x n matrix

selected_headers, lengths = [], []           # headers with length 0 or 1, length of set
for i, header in enumerate(headers):
    if len(set(df[header])) == 1:
        selected_headers.append(header)

        if df[header][0] == "NULL_VALUE":
            lengths.append(0)
        else:
            lengths.append(1)
    elif len(set(df[header])) == 2:
        if "NULL_VALUE" in set(df[header]):
            selected_headers.append(header)
            lengths.append(1)
selected_headers = [selected_header.replace("\n", " ") for selected_header in selected_headers]
# ^^ Some of the headers have an "\n" in them. ^^

with open("results.txt", "w") as f:
    for i, length in enumerate(lengths):
        f.writelines(f"{selected_headers[i]}\t{lengths[i]}\n")
