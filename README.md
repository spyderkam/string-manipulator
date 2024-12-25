# Text and File Processing Utilities

A Python library providing utilities for text processing, file manipulation, and data extraction. Includes functionality for finding strings, splitting files, and processing specialized log files.

## Features

- String search and position finding
- File splitting by:
  - Number of files
  - Number of lines
  - File size
- Log file processing:
  - Timestamp extraction
  - URN (Unique Reference Number) message filtering
- Output to various formats (CSV, DAT, etc.)

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
```

2. Required dependencies:
```bash
pip install numpy pandas
```

## Usage

### Text Class

The `Text` class provides methods for text manipulation and file operations.

#### Finding Strings
```python
from text_utils import Text

# Initialize with text content
text = Text(input_text)

# Find occurrences and positions of a string
count, positions = text.find_string("search_term")
```

#### Dividing Files
```python
# Divide into n files
text.divide_by_lines(
    No_lines=1000,     # Total number of lines
    divfiles=10,       # Number of output files
    folder='output',   # Output directory
    ext='dat'          # Output file extension
)

# Split by maximum lines per file
text.split_by_lines(
    divlines=100,      # Max lines per file
    ext='txt',         # Output extension
    folder='output'    # Output directory
)

# Split by file size
text.split_by_size(
    size=1024,         # Size in bytes
    ext='txt',         # File extension
    folder='output',   # Output directory
    fname='split'      # Base filename
)
```

### ExSpread Class

The `ExSpread` class handles specialized log file processing and data extraction.

#### Extracting Timestamps
```python
from text_utils import ExSpread

# Initialize with file path and search string
log_processor = ExSpread(
    "path/to/log.ascii_out",
    "search_string"
)

# Extract timestamps to CSV
log_processor.mk_timesheet(
    folder='output',
    fname='timestamps'
)
```

#### Processing URN Messages
```python
# Initialize with file path and URN
urn_processor = ExSpread(
    "path/to/log.ascii_out",
    "696683"  # URN can be string or integer
)

# Extract URN messages
urn_processor.find_URN_messages(
    folder='output',
    fname='urn_messages'
)
```

## Output Formats

### File Naming Conventions
- Split files: `i_file.ext` or `splittedFile_i.ext` (i starting from 0)
- URN messages: `[filename].dat`
- Timestamps: `[parent_directory]_[filename].CSV`

### Directory Structure
Output files are automatically organized in specified directories. If a directory doesn't exist, it will be created.

## Limitations

- Text processing methods work with UTF-8 encoded files
- File splitting may result in uneven distribution in the last file
- URN message extraction requires specific log file format
- Timestamp extraction expects specific formatting in log files

## Contributing

Feel free to submit pull requests or create issues for:
- Bug fixes
- New features
- Documentation improvements
- Performance optimizations

## License

This project is licensed under the MIT License. See the (LICENSE)[https://github.com/spyderkam/string-manipulator/blob/main/LICENSE] file for details.


## Notes

- Method implementations prioritize functionality over efficiency in some cases
- Directory creation uses shell commands and may require adjustments for different operating systems
- Some methods are tailored for specific log file formats (`.ascii_out` files)
