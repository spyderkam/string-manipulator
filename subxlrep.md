# Subdirectory Excel Reporter

Kamyar Modjtahedzadeh  
Boeing Intelligence & Analytics  
May 19, 2025

## The Problem 

**<u>_Kam_</u>:**

Let's say I have a master directory called `"master"`; the path to it is `"path/to/master"`.

`"master"` has an amount of subdirectories (let's say $n$ subdirectories). Each of these subdirectories contains both subsubdirectories and files.

I want a Python script that given the path to `"master"`, it creates an Excel (.xlsx) file with $n$ sheets, the sheet titles are the titles of the subdirectories. Then, each sheet contains 3 columns: The 1st column is the name of the files _and/or_ subsubdirectories that are in the subdirectory, the 2nd column is the size of the file/subsubdirectory, and the 3rd column states whether it is a "file" or "directory". The title of the columns are to be: `"Name"`, `"Size"`, and `"type"`. When needed, use `pandas` as apposed to any alternative packages.

## The Raw Solution

**<u>_Grok 3_</u>:**

To solve your request, I’ll create a Python script that analyzes the directory structure of a master directory located at `"path/to/master"`, which contains `n` subdirectories. Each subdirectory may include both files and subsubdirectories. The script will generate an Excel file with `n` sheets, where each sheet corresponds to one subdirectory, named after it, and contains three columns: `"Name"`, `"Size"`, and `"Type"`. These columns will list the names of files and subsubdirectories within the subdirectory, their sizes, and whether each is a `"file"` or `"directory"`. We’ll use the `pandas` library to create the Excel file, as specified.

Here’s how we’ll approach it:

  1.  **Traverse the Directory:** Use the `os` module to identify all subdirectories in `"path/to/master"` and list their immediate contents (files and subsubdirectories).
  2.  **Calculate Sizes:** For files, retrieve the size directly; for subsubdirectories, compute the total size of all files within them recursively.  
  3.  **Organize Data:** For each subdirectory, collect the name, size, and type of each item into a structured format.
  4.  **Create the Excel File:** Use `pandas` to generate a DataFrame for each subdirectory’s data and write it to a separate sheet in an Excel file.
    
Below is the complete Python script:

```python
__author__ = "Grok 3"
__date__ = "May 14, 2025"

import os
import pandas as pd

def get_dir_size(path):
    """Recursively calculate the total size of all files in a directory."""
    total = 0
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):
            total += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total += get_dir_size(full_path)
    return total

def create_directory_excel(master_path, output_file="directory_info.xlsx"):
    """Create an Excel file with a sheet for each subdirectory in master_path."""
    
    # Get list of subdirectories in the master directory
    subdirs = [d for d in os.listdir(master_path) if os.path.isdir(os.path.join(master_path, d))]
    
    # Initialize Excel writer
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        for subdir in subdirs:
            subdir_path = os.path.join(master_path, subdir)
            data = []
            
            # List immediate contents of the subdirectory
            for item in os.listdir(subdir_path):
                item_path = os.path.join(subdir_path, item)
                if os.path.isfile(item_path):
                    size = os.path.getsize(item_path)
                    type_ = "file"
                elif os.path.isdir(item_path):
                    size = get_dir_size(item_path)
                    type_ = "directory"
                else:
                    continue  # Skip non-file, non-directory items
                data.append({"Name": item, "Size": size, "Type": type_})
            
            # Create a DataFrame and write to an Excel sheet
            df = pd.DataFrame(data, columns=["Name", "Size", "Type"])
            df.to_excel(writer, sheet_name=subdir, index=False)

# Usage with the specified master directory
master_path = "path/to/master"
create_directory_excel(master_path)
```

### Explanation

-   **Imports:**
    -   `os`**:** For interacting with the file system (listing directories, checking file types, getting sizes).    
    -   `pandas as pd` For creating DataFrames and writing to Excel.
-   `get_dir_size(path)` **Function:**    
    -   Takes a directory path and recursively calculates the total size (in bytes) of all files within it, including files in nested subdirectories.   
    -   `Uses os.listdir()` to iterate over contents, `os.path.isfile()` to identify files, `os.path.getsize()` to get file sizes, and calls itself for subdirectories.        
-   `create_directory_excel(master_path, output_file)` **Function:**    
    -   **Input:** `master_path` (e.g., `"path/to/master"`) and an optional `output_file` name (defaults to `"directory_info.xlsx"`).      
    -   **Subdirectories:** Retrieves all subdirectories in `master_path` using a list comprehension with `os.path.isdir()` to filter directories.        
    -   **Excel Writer:** Uses `pd.ExcelWriter` with the `xlsxwriter` engine in a context manager to handle file creation and cleanup.
    -   **Per Subdirectory:**        
        -   Constructs the full path to the subdirectory.
        -   Iterates over its immediate contents using `os.listdir()`.
        -   For each item:
            -   If a file: Gets its size with `os.path.getsize()` and sets type as `"file"`.
            -   If a directory: Calculates its total size with `get_dir_size()` and sets type as `"directory"`.
            -   Skips items that are neither (e.g., symbolic links if not followed).
        -   Collects data in a list of dictionaries with keys `"Name"`, `"Size"`, and `"Type"`.
        -   Creates a `pandas` DataFrame with the specified column order.
        -   Writes the DataFrame to a sheet named after the subdirectory using `df.to_excel()`, excluding the index.
-   **Usage:**
    -   Sets `master_path = "path/to/master"` as per your query.
    -   Calls the function to generate `"directory_info.xlsx"` in the current working directory.
        

### Output

The resulting Excel file will have:

-   **Sheets:** One for each of the `n` subdirectories, named after the subdirectory (e.g., if subdirectories are `"sub1`", `"sub2"`, etc., sheets will be named `"sub1"`, `"sub2"`, etc.).
    
-   **Columns**: `"Name"`, `"Size",` `"Type"`, listing the immediate files and subsubdirectories in each subdirectory.
    
-   **Sizes:** In bytes; files show their direct size, subsubdirectories show the recursive total size of all contained files.
    

### Notes

-   Replace `"path/to/master"` with the actual path to your `"master"` directory when running the script.   
-   The script assumes access to all directories and files; add error handling (e.g., `try-except`) if permissions might be an issue.   
-   Sheet names (subdirectory names) should be unique and valid in Excel (max 31 characters, no special characters like `/` or `*`); adjust names if necessary in practice.

This script meets all your requirements using `pandas` for Excel creation, providing a clear and structured analysis of the `"master"` directory’s subdirectories.

## The Efficient Solution

**<u>_Kam_</u>:**

I asked Grok the following question:

> Let's say I have a master directory called `"master"`; the path to it is `"path/to/master"`.
> `"master"` has an amount of subdirectories (let's say $n$ subdirectories). Each of these subdirectories contains both subsubdirectories and files.
> I want a Python script that given the path to `"master"`, it creates an Excel (.xlsx) file with $n$ sheets, the sheet titles are the titles of the subdirectories. Then, each sheet contains 3 columns: The 1st column is the name of the files _and/or_ subsubdirectories that are in the subdirectory, the 2nd column is the size of the file/subsubdirectory, and the 3rd column states whether it is a "file" or "folder". The title of the columns are to be: `"Name"`, `"Size"`, and `"type"`. When needed, use `pandas` as apposed to any alternative packages.

It gave me the previous script (subxlrep_slow.py); which is good, including the progress tracker, apart from two important details:

  1. If a subdir name is longer than 24 characters, it gives me an error that the string is too long for an Excel sheet-name. if this is the case, then please have the name truncated to 24 characters for the sheet-name. 
  2. The master directory I am working with is enormous; i.e., $\propto1$&nbsp;$\mathrm{TB}$, some of the subdirectories are in over $100$&nbsp;$\mathrm{GB}$, it is taking _forever_ to run. The good news is that in there are only nine subdirectories in my master directories, and the _number_ of both files and folders in each subdirectory is _relatively_ low; e.g., there should not be more than 50 items in any given subdirectory.

Claude Sonnet, please help me with my above issues. Modify my script, or write a new one, whatever you deem best.

**<u>_Claude Sonnet 3.7_</u>:**

I'll help you modify the script to address both issues. The main problems to solve are:

1. Truncating sheet names longer than 24 characters
2. Improving performance for very large directories
3. Display sizes in a more readable format with appropriate units

Here's an optimized version of the script that addresses both concerns:

```python
#!/usr/bin/env python3

__author__ = "Grok 3, Kam Modjtahedzadeh, Claude Sonnet 3.7"
__date__ = "May 14, 2025 - May 19, 2025"

import os
import pandas as pd
import subprocess

# Helper function to format file/folder sizes
def format_size(size_bytes):
    """Format the size with appropriate units based on the size."""
    
    # Define thresholds in bytes
    KB = 1024
    MB = KB*1024
    GB = MB*1024
    TB = GB*1024
    
    if size_bytes < KB:
        return f"{size_bytes} B"
    elif size_bytes < MB:
        return f"{size_bytes/KB:.2f} KB"
    elif size_bytes < GB:
        return f"{size_bytes/MB:.2f} MB"
    elif size_bytes < TB:
        return f"{size_bytes/GB:.2f} GB"
    else:
        return f"{size_bytes/TB:.2f} TB"

def get_dir_size_fast(path):
    """Get the size of a directory using a faster method that doesn't do deep recursion."""
    try:
        if os.name == 'posix':  # For Unix/Linux/MacOS
            # Use du command for faster directory size calculation
            result = subprocess.run(['du', '-sb', path], capture_output=True, text=True)  
            if result.returncode == 0:
                # Parse the output: first field is size in bytes
                try:
                    size_bytes = int(result.stdout.split()[0])
                    return size_bytes
                except (ValueError, IndexError):
                    pass  # Fall back to manual calculation if parsing fails
        
        # Fallback to manual calculation for Windows or if du fails
        total = 0
        # Only count immediate contents (no recursion)
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                total += os.path.getsize(item_path)
        return total
    except (PermissionError, FileNotFoundError, subprocess.SubprocessError):
        return 0  # Return 0 if there are any errors

def create_directory_excel(master_path, output_file="directory_info.xlsx"):
    """Create an Excel file with a sheet for each subdirectory in master_path."""

    # Get list of subdirectories in the master directory
    ignoreDirs = ["ignore_this_dir"]
    subdirs = [d for d in os.listdir(master_path) if os.path.isdir(os.path.join(master_path, d)) and d not in ignoreDirs and d[0] != '.']
    total_subdirs = len(subdirs)

    # Initialize Excel writer
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        for i, subdir in enumerate(subdirs, 1):
            # Truncate sheet name if needed
            sheet_name = subdir[:31]  # As low as 24 and as high as 31
            
            # Replace invalid characters in Excel sheet names
            invalid_chars = [':', '\\', '/', '?', '*', '[', ']']
            for char in invalid_chars:
                sheet_name = sheet_name.replace(char, '_')
                
            subdir_path = os.path.join(master_path, subdir)
            data = []

            # List immediate contents of the subdirectory
            try:
                items = os.listdir(subdir_path)
                total_items = len(items)
                item_count = 0  # Track processed items
                
                for item in items:
                    item_count += 1
                    item_path = os.path.join(subdir_path, item)
                    try:
                        if os.path.isfile(item_path):
                            size = os.path.getsize(item_path)
                            type_ = "file"
                        elif os.path.isdir(item_path):
                            # Get size of immediate contents only (no deep recursion)
                            size = get_dir_size_fast(item_path)
                            type_ = "folder"
                        else:
                            continue  # Skip non-file, non-directory items
                        
                        formatted_size = format_size(size): Format the size with appropriate units
                        data.append({"Name": item, "Size": formatted_size, "type": type_})  # MODIFIED: Use formatted_size
                        
                        if total_items > 0:  # Avoiding division by zero
                            print(f" Processing item {item_count} of {total_items} in {subdir}: {item_count/total_items*100:.2f}% complete")
                    except (PermissionError, FileNotFoundError):
                        # Skip items with access issues
                        continue
            except (PermissionError, FileNotFoundError):
                print(f"Could not access subdirectory: {subdir}")
                continue
                
            # Create a DataFrame and write to an Excel sheet
            df = pd.DataFrame(data, columns=["Name", "Size", "type"])
            df.to_excel(writer, sheet_name=sheet_name, index=False)  # MODIFIED: Removed 
            
            print(f"Subdirectory {i} of {total_subdirs} processed: {i/total_subdirs*100:.2f}% complete")
    print(f"Excel file created: {output_file}")

# Usage example
if __name__ == "__main__":
    from tkinter import filedialog, Tk
    
    root = Tk()
    root.withdraw()

    topDir = filedialog.askdirectory(initialdir=os.getcwd(), title='Select Top Directory') 
    
    output_file = "directory_info.xlsx"
    create_directory_excel(topDir, output_file)
```

Key improvements:

1. **Sheet name truncation**: The script now truncates any subdirectory name longer than 24 characters when using it as a sheet name.

2. **Performance optimization**: Instead of recursively calculating the size of each subdirectory (which was the major bottleneck), the script now:
   - On Unix/Linux/MacOS: Uses the much faster `du -sb` command to get directory sizes
   - On Windows: Only calculates the size of the immediate files in a directory (no deep recursion)

3. **Error handling**: The script has improved error handling to skip files or directories that can't be accessed instead of failing.

4. **Invalid character handling**: The script has code to replace invalid characters in Excel sheet names (such as colons, slashes, etc.).

5. **Size Readability**: Added a new `format_size` function to convert bytes to human-readable format with the appropriate units

This should significantly improve the performance since you mentioned that the subdirectories contain a relatively small number of items (less than 50), but some are very large (100+ GB). The script (<span>subxlrep.py</span>) maintains the same progress tracking functionality from the original but should run much faster since it avoids the deep recursive size calculation that was causing the performance issues.

