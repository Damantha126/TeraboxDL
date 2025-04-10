# TeraboxDL 🚀

TeraboxDL is a Python package designed to interact with Terabox, enabling you to retrieve file details such as file names, direct download links, thumbnails, and file sizes.

## Features ✨

- 🔍 Fetch file details from Terabox links.
- 📥 Extract direct download links for files.
- 🖼️ Retrieve file thumbnails and sizes.
- 📂 Download files directly to a specified directory.
- ⚠️ Handle errors gracefully with detailed error messages.
- 📊 Display a progress bar during file downloads or use a custom callback for real-time progress tracking.
- 🛠️ Automatically create directories for saving files if they do not exist.
- 🐍 Support for Python 3.7 or higher.



## Installation

Install the package via pip:

```bash
pip install terabox-downloader
```

## Usage

Below is an example of how to use the TeraboxDL package:

```python
from TeraboxDL import TeraboxDL

# Initialize the TeraboxDL instance with your cookie
cookie = "your_cookie_here" # Ex: "lang=en; ndus="
terabox = TeraboxDL(cookie)

# Retrieve file information from a Terabox link
link = "https://www.terabox.app/s/your_link_here"
file_info = terabox.get_file_info(link, direct_url=True)

# Check if there was an error retrieving the file information
if "error" in file_info:
    print("Error:", file_info["error"])
    exit()

# Print the retrieved file information
print("File Name:", file_info["file_name"])
print("Download Link:", file_info["download_link"])
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
- `direct_url` (bool, optional): If set to `True`, the method will return a direct download link instead of the default download link. Defaults to `False`.

**Returns:**

A dictionary containing the following keys:
- `file_name` (str): The name of the file.
- `download_link` (str): The download link for the file. If `direct_url` is `True`, this will be a direct download link.
- `thumbnail` (str): The URL of the file's thumbnail.
- `file_size` (str): The size of the file in a human-readable format (e.g., MB, KB).
- `sizebytes` (int): The size of the file in bytes.
- `error` (str, optional): An error message if something goes wrong.

---

## Downloading Files

The `download()` method allows you to download files from Terabox using the file information retrieved by the `get_file_info()` method.

### Method: `download(file_info: dict, save_path: str = None)`

#### Parameters:
- **`file_info`** *(dict)*: A dictionary containing file information, including:
  - `file_name` *(str)*: The name of the file to be downloaded.
  - `download_link` *(str)*: The direct download link for the file.
- **`save_path`** *(str, optional)*: The directory path where the file should be saved. If not provided, the file will be saved in the current directory.
- **`callback`** *(callable, optional)*: A callback function that receives progress updates with parameters (downloaded_bytes, total_bytes, percentage)

#### Returns:
- *(dict)*: A dictionary containing:
  - `file_path` *(str)*: The path to the downloaded file, if successful.
  - `error` *(str)*: An error message, if an error occurs.

#### Example Usage:
```python
from TeraboxDL import TeraboxDL

# Initialize the TeraboxDL instance with a valid cookie
terabox = TeraboxDL(cookie="your_cookie_here")

# Retrieve file information
file_info = terabox.get_file_info("https://www.terabox.com/s/your_link_here")

# Download the file
if "error" not in file_info:
    result = terabox.download(file_info, save_path="downloads/")
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"File downloaded to: {result['file_path']}")
else:
    print(f"Error: {file_info['error']}")
```
### Notes

- Ensure that the `file_info` dictionary contains valid `file_name` and `download_link` keys.
- If the `save_path` is provided, it must be a valid directory. The method will create the directory if it does not exist.
- The method displays a progress bar during the download process.
- Handle exceptions gracefully to ensure smooth execution.

### Using the `callback` Parameter in `download()`

The `download()` method supports an optional `callback` parameter that allows you to monitor the download progress programmatically. The `callback` function is called during the download process with the following parameters:

#### Callback Parameters:
- **`downloaded_bytes`** *(int)*: The number of bytes downloaded so far.
- **`total_bytes`** *(int)*: The total size of the file in bytes. If the size is unknown, this will be `0`.
- **`percentage`** *(float)*: The percentage of the file downloaded so far.

#### Example Usage:
```python
# Define a callback function to monitor progress
def progress_callback(downloaded_bytes, total_bytes, percentage):
    print(f"\rDownloaded: {downloaded/1024/1024:.2f} MB / {total/1024/1024:.2f} MB ({percentage:.1f}%)", end="")

# Download the file with a callback
if "error" not in file_info:
    result = terabox.download(file_info, save_path="downloads/", callback=progress_callback)
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"File downloaded to: {result['file_path']}")
else:
    print(f"Error: {file_info['error']}")
```

### Notes

- The `callback` function is invoked for each chunk of data downloaded, allowing you to track progress in real-time.
- If no `callback` is provided, a terminal-based progress bar (powered by `tqdm`) is displayed by default.
- Use the `callback` parameter for custom progress handling, such as updating a graphical user interface (GUI), logging progress to a file, or integrating with other monitoring tools.
- Ensure that the `callback` function is designed to handle frequent updates efficiently to avoid performance bottlenecks during downloads.
- The `total_bytes` parameter in the `callback` may be `0` if the file size is unknown, so handle such cases appropriately in your implementation.
- This feature provides flexibility for developers to tailor the download experience to their specific needs.
- Example use cases include displaying progress in a web application or sending periodic updates to a remote server.
- For simple use cases, the default progress bar is sufficient and requires no additional setup.
- Always test your `callback` implementation to ensure it behaves as expected under various network conditions.


## Requirements

- Python 3.7 or higher

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Damantha126/TeraboxDL/blob/main/LICENSE) file for more details.
