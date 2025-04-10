TeraboxDL is a Python package designed to interact with Terabox, enabling you to retrieve file details such as file names, direct download links, thumbnails, and file sizes.

## Features

- Fetch file details from Terabox links.
- Extract direct download links for files.
- Convert file sizes into human-readable formats.
- Simple and asynchronous API.

## Installation

Install the package via pip:

```bash
pip install terabox-downloader
```

## Usage

Below is an example of how to use the TeraboxDL package:

```python
from TeraboxDL import TeraboxDL
import asyncio

# Initialize the TeraboxDL instance with your cookie
cookie = "your_cookie_here" # Ex: "lang=en; ndus="
terabox = TeraboxDL(cookie)

# Retrieve file information from a Terabox link
link = "https://www.terabox.app/s/your_link_here"
file_info = terabox.get_file_info(link)

# Check if there was an error retrieving the file information
if "error" in file_info:
    print("Error:", file_info["error"])
    exit()

# Print the retrieved file information
print("File Name:", file_info["file_name"])
print("Direct Link:", file_info["download_link"])
print("Thumbnail:", file_info["thumbnail"])
print("File Size:", file_info["file_size"])

```

## Methods

### `TeraboxDL(cookie: str)`
Initializes the `TeraboxDL` instance.

**Parameters:**
- `cookie` (str): The authentication cookie string.

---

### `get_file_info(link: str) -> dict`
Fetches file details from a Terabox link.

**Parameters:**
- `link` (str): The Terabox link to process.

**Returns:**
A dictionary containing:
- `file_name`: Name of the file.
- `download_link`: Direct download link.
- `thumbnail`: Thumbnail URL.
- `file_size`: Human-readable file size.
- `sizebytes`: File size in bytes.

---

## Requirements

- Python 3.7 or higher

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Damantha126/TeraboxDL/blob/main/LICENSE) file for more details.
