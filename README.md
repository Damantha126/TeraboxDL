# TeraboxDL 🚀

TeraboxDL is a Python package for interacting with Terabox, enabling you to fetch file details such as name, download link, thumbnail, and size, and download files with support for custom progress tracking via a callback function.

---

## 🌟 Features

- 🔗 Get direct download links from Terabox.
- 📝 View file name, size, and thumbnail.
- 📥 Download files to any folder.
- 📊 Built-in or custom progress bar support.
- ❌ Handles errors with helpful messages.
- 🐍 Works with Python 3.7 and above.

---

## ⚙️ Installation

Install using pip:

```bash
pip install terabox-downloader
```

---

## 🍪 How to Get the Cookie
<details>
<summary><b>Click here for the tutorial</b></summary>

To use TeraboxDL, you need to provide your Terabox cookie. Here's how you can get it:

1. Open your `Edge browser` and log in to your Terabox account.
2. Click the padlock icon next to the URL in the address bar and Click `Permissions for this site`.
3. In the pop-up, click `Cookies and site data`.
4 Then click `Cookies (X cookies in use)` to open the cookies viewer.
5. Under the `terabox.com domain`, expand the Cookies section.
5. Look for the `lang` and `ndus` cookies. Copy their values and combine them in the format:  
    `lang=your_lang_value; ndus=your_ndus_value;`

#### Example: 
````python
cookie = "lang=en; ndus=Y**********a;"
````
#### 📝 You can now use this cookie string in tools or scripts that require authentication with TeraBox.

### For a visual guide, refer to the image below:

![How to Get Cookie](https://raw.githubusercontent.com/Damantha126/TeraboxDL/refs/heads/main/HowToGetCookies.png)

</details>

## 🚀 Quick Start

```python
from TeraboxDL import TeraboxDL

# Step 1: Add your Terabox cookie
cookie = "your_cookie_here"  # e.g., "lang=en; ndus="

# Step 2: Create an instance of TeraboxDL
terabox = TeraboxDL(cookie)

# Step 3: Paste your file link
link = "https://www.terabox.app/s/your_link_here"

# Step 4: Get file info
file_info = terabox.get_file_info(link)

# Step 5: Check for errors and show info
if "error" in file_info:
    print("Error:", file_info["error"])
else:
    print("File Name:", file_info["file_name"])
    print("Download Link:", file_info["download_link"])
    print("Thumbnail:", file_info["thumbnail"])
    print("File Size:", file_info["file_size"])
```

---

## 📂 Downloading Files

```python
# Download file
result = terabox.download(file_info, save_path="downloads/")

if "error" in result:
    print("Error:", result["error"])
else:
    print("✅ Downloaded to:", result["file_path"])
```

You can also show a **custom progress bar** using a callback:

```python
def progress_callback(downloaded, total_size, percentage):
    done = int(50 * downloaded / total_size)
    print(f"\r[{'=' * done}{' ' * (50 - done)}] {downloaded / total_size * 100:.2f}%", end='')

# Use callback
result = terabox.download(file_info, save_path="downloads/", callback=progress_callback)
```

---

## 📘 API Overview

### `TeraboxDL(cookie)`
Create an instance with your Terabox cookie.

### `get_file_info(link)`
Returns file info:
- `file_name`, `download_link`, `thumbnail`, `file_size`, `sizebytes`
- If something goes wrong: `error`

### `download(file_info, save_path=None, callback=None)`
Downloads the file using info from `get_file_info`.

Returns:
- `file_path` if successful
- `error` if failed

---

## 🔧 Notes

- `save_path` is optional; defaults to the current folder.
- Directory is auto-created if it doesn’t exist.
- If `callback` is not provided, a default terminal progress bar is shown.
- `callback` gives real-time download updates (bytes and %).
- Use `callback` for GUI apps, bots, web interfaces, or logs.

---

## 📦 Requirements

- Python 3.7+

---

## 📝 License

MIT License. See [LICENSE](https://github.com/Damantha126/TeraboxDL/blob/main/LICENSE).
