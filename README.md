# Python Text and File Processing Utilities

A comprehensive Python library providing utilities for text processing, file manipulation, data extraction, and various file format handling. The toolkit includes functionality for string operations, file splitting, log processing, and specialized data format handling.

## Features

### Text and File Processing
- String search and position finding with support for regular expressions
- File splitting with customizable size and format options
- Log file processing with timestamp and message extraction
- Indentation conversion between 2 and 4 spaces
- String replacement across multiple files with backup creation
- Excel column letter/header conversion with support for complex spreadsheets
- HDF5 file analysis and variable extraction
- Empty column filtering for spreadsheet optimization

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
```

2. Install required dependencies:
```bash
pip install numpy pandas h5py xlsxwriter fileinput
```

## Components

### Text Processing (string_manipulator.py)

The `Text` class provides core text manipulation and file operations with support for various file formats and encoding types.

```python
from string_manipulator import Text

# Initialize with text content
text = Text(input_text)

# Find occurrences and positions of a string
count, positions = text.find_string("search_term")
# Returns: (3, [0, 45, 72]) # Example: 3 occurrences at positions 0, 45, and 72

# Split files with custom configuration
text.divide_by_lines(
    No_lines=1000,  # Total number of lines in input file
    divfiles=10,    # Number of output files desired
    folder='output',# Output directory
    ext='dat'       # Output file extension
)

# Split by maximum lines per file
text.split_by_lines(
    divlines=100,   # Maximum lines per output file
    ext='txt',      # Output file extension
    folder='output' # Output directory
)

# Split by file size with custom naming
text.split_by_size(
    size=1024,      # Size in bytes
    ext='txt',      # Output file extension
    folder='output',# Output directory
    fname='split'   # Base filename for output files
)
```

### Indentation Converter (indent_converter.py)

Convert between 2-space and 4-space indentation in Python files with backup creation and error handling.

```python
from indent_converter import convert_indentation

# Convert to 2 spaces
convert_indentation(
    "path/to/file.py",
    to_two_spaces=True  # False for 4-space conversion
)

# Error handling example
try:
    convert_indentation("path/to/file.py", to_two_spaces=True)
except Exception as err:
    print(f"Error processing file: {str(err)}")
```

Configuration Options:
- `to_two_spaces`: Boolean flag for conversion direction
- Automatic backup creation with `.bak` extension
- Preserves empty lines and comments
- Handles mixed indentation gracefully

### Excel Column Utilities (letters_and_headers.py)

Comprehensive utilities for working with Excel column letters and headers, supporting complex spreadsheet operations.

```python
from letters_and_headers import (
    getLetters, 
    getHeaders, 
    colLetter_to_Num,
    colHeader_to_Letter,
    stringOfLettersList
)

# Convert headers to Excel column letters
letters = getLetters(['Name', 'Age'], dataframe)
# Returns: {'Name': 'A', 'Age': 'B'}

# Convert letters to headers
headers = getHeaders(['A', 'B'], dataframe)
# Returns: {'A': 'Name', 'B': 'Age'}

# Convert column letter to number (zero-based)
column_num = colLetter_to_Num('AA')
# Returns: 26 (zero-based index)

# Get formatted string of column letters
letters_str = stringOfLettersList(['Name', 'Age'], dataframe)
# Returns: "A, B"

# Convert multiple headers to letter format
column_letters = colHeader_to_Letter(['Name', 'Age'], dataframe)
# Returns: "A, B"
```

### HDF5 File Processing (hdf5.py)

Advanced tools for analyzing and processing HDF5 files with support for complex data structures and variable types.

```python
from hdf5 import HDF5

# Initialize HDF5 processor
h5_file = HDF5("path/to/file.h5")

# Find variables in HDF5 file
var_locations = h5_file.findVar('variable_name')
# Returns: {'dataset_name': [0, 2, 5]} # Indices where variable appears

# Generate complete data sets
h5_dict, h5_varNames, varNames = h5_file.genSets()

# Access specific variables
if 'Time' in varNames:
    time_locations = h5_file.findVar('Time')
    print(f"Time variable found in: {time_locations}")
```

Key Features:
- Support for complex HDF5 data structures
- Efficient variable search and extraction
- Comprehensive data set generation
- Error handling for invalid HDF5 files
- Memory-efficient processing of large files

### Empty Column Filter (empty_column_filter.py)

Identify and filter empty or single-value columns in spreadsheets with detailed analysis capabilities.

```python
# Configuration
ms = "Master_1_052024_GOLDEN_RUNS.xlsx"
df = pd.read_excel(ms, sheet_name="Main Sheet", skiprows=0)

# Customization options
df.fillna(value="NULL_VALUE", inplace=True)  # Custom null value marker
headers = df.columns

# Results processing
selected_headers = []  # Headers with 0 or 1 unique values
lengths = []          # Number of unique values

# Output format in results.txt:
# Column_Name    Unique_Values_Count
# Date          1
# Status        0
```

Features:
- Custom null value handling
- Support for multi-sheet Excel files
- Handles newline characters in headers
- Detailed analysis output
- Memory-efficient processing

### String Replacement

The library provides both Python and Bash implementations for replacing strings across multiple files in a directory.

#### Bash Implementation
Create a file called `replace_string.sh`:

#### Python Implementation
Create a file called `replace_string.py`:

```python
import os
import fileinput

def replace_string_in_files(old_string, new_string, directory):
    """
    Replace strings in all files within a directory.
    
    Args:
        old_string (str): String to replace
        new_string (str): Replacement string
        directory (str): Target directory path
        
    Features:
        - Recursive directory traversal
        - Automatic backup creation
        - UTF-8 encoding support
        - Error handling
    """
    for root, dirs, files in os.walk(directory):
        for filename in files:
            try:
                file_path = os.path.join(root, filename)
                with fileinput.FileInput(
                    file_path, 
                    inplace=True, 
                    backup='.bak'
                ) as file:
                    for line in file:
                        print(line.replace(old_string, new_string), end='')
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python replace_string.py OLD_STRING NEW_STRING DIRECTORY")
        sys.exit(1)

    old_string = sys.argv[1]
    new_string = sys.argv[2]
    directory = sys.argv[3]

    replace_string_in_files(old_string, new_string, directory)
```

Key Features:
- Recursive directory traversal
- Automatic backup creation (.bak files)
- UTF-8 encoding support
- Comprehensive error handling
- Progress feedback

Usage:
```bash
python replace_string.py "old_text" "new_text" /path/to/directory
```

```bash
#!/bin/bash

# Usage: ./replace_string.sh "old_string" "new_string" /path/to/directory

OLD_STRING=$1
NEW_STRING=$2
DIRECTORY=$3

# Check if all arguments are provided
if [ -z "$OLD_STRING" ] || [ -z "$NEW_STRING" ] || [ -z "$DIRECTORY" ]; then
  echo "Usage: $0 OLD_STRING NEW_STRING DIRECTORY"
  exit 1
fi

# Find and replace
find "$DIRECTORY" -type f -exec sed -i '' "s/$OLD_STRING/$NEW_STRING/g" {} +

echo "Replacement completed."
```

Key Features:
- Argument validation
- Directory-wide search
- In-place file modification
- Progress feedback

Usage:
```bash
./replace_string.sh "old_text" "new_text" /path/to/directory
```

### Log Processing (ExSpread class)

Advanced log file processing with support for various formats and data extraction patterns.

```python
from string_manipulator import ExSpread

# Timestamp extraction
log_processor = ExSpread(
    "path/to/log.ascii_out",
    "search_string"
)
log_processor.mk_timesheet(
    folder='output',
    fname='timestamps'
)

# URN message processing
urn_processor = ExSpread(
    "path/to/log.ascii_out",
    "696683"  # URN as string or integer
)
urn_processor.find_URN_messages(
    folder='output',
    fname='urn_messages'
)
```

## File Format Requirements

### HDF5 Files
- Must be valid HDF5 format
- Should contain variable names matching search patterns
- Requires appropriate read permissions
- File size handling depends on available memory

### Excel Files
- Supports .xlsx, .xls, and .csv formats
- Headers must be in first row unless specified
- Column names should be unique
- Special characters in headers are supported
- Large files may require batch processing

### Log Files
- UTF-8 encoding required
- Timestamp format: "YYYY-MM-DD HH:MM:SS"
- URN messages must follow specified format
- Line endings must be consistent

### Text Files
- UTF-8 encoding recommended
- Line endings must be consistent
- File permissions must allow read/write
- Backup space required for operations

## Limitations

### Text Processing
- Memory constraints for very large files
- Regular expression performance varies with pattern complexity
- Backup creation requires additional storage space
- Some operations are not atomic

### Excel Processing
- Column limit of 16,384 (XLS) or 16,777,216 (XLSX)
- Memory usage scales with file size
- Some formula types may not be preserved
- Conditional formatting may be lost

### HDF5 Processing
- Limited support for custom data types
- Memory requirements scale with dataset size
- Nested group depth may affect performance
- Some metadata may not be preserved

### Log Processing
- Specific format requirements
- Time zone handling limitations
- Performance degrades with file size
- Limited support for compressed logs

## Error Handling

The library implements comprehensive error handling:

1. File Operations:
   - FileNotFoundError for missing files
   - PermissionError for access issues
   - Encoding errors for text files

2. Data Processing:
   - ValueError for invalid data
   - TypeError for mismatched data types
   - Memory errors for large datasets

3. Format-Specific:
   - HDF5 format validation
   - Excel worksheet validation
   - Log format verification

4. Recovery:
   - Automatic backup creation
   - Transaction rollback where applicable
   - Error logging and reporting

## Contributing

Detailed contribution guidelines:

1. Code Style:
   - Follow PEP 8
   - Include docstrings
   - Add type hints
   - Write unit tests

2. Pull Requests:
   - Create feature branch
   - Add tests
   - Update documentation
   - Follow commit message format

3. Testing:
   - Run existing test suite
   - Add new test cases
   - Include edge cases
   - Test with large datasets

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/spyderkam/string-manipulator/blob/main/LICENSE) file for details.

## Notes

Development Considerations:
- Performance optimization prioritizes reliability
- Memory management focuses on large file handling
- Error handling emphasizes data preservation
- Backup creation may impact storage requirements
- Cross-platform compatibility may vary
- Some operations require administrative privileges
- logging module integration recommended
- Consider batch processing for large datasets
