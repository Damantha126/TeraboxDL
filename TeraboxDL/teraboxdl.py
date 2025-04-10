import sys
import os
import tqdm
import requests
from datetime import date
from .__version__ import __version__
from urllib.parse import urlparse, parse_qs, unquote

# URL for fetching configurations
CONFIGS="https://gist.githubusercontent.com/Damantha126/98270168b0d995f33d6d021746e1ce2f/raw/terabox_config.json"

# Fetch configurations from the URL
try:
    req = requests.get(CONFIGS).json()
except:
    req = {"LAST_VERSION": __version__}

class TeraboxDL:
    """
    A Python class to interact with Terabox and retrieve file information.
    """

    notice_displayed = False
    def __init__(self, cookie: str):
        """
        Initialize the TeraboxDL instance with the required cookie.

        Args:
            cookie (str): The cookie string required for authentication.
        """
        if not cookie:
            raise ValueError("Cookie cannot be empty.")
        self.cookie = cookie
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
            "Connection": "keep-alive",
            "DNT": "1",
            "Host": "www.terabox.app",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
            "sec-ch-ua": '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            "Cookie": self.cookie,
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        }
        self.dlheaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.terabox.com/',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cookie':self.cookie
        }
        # Initialize notice_displayed flag
        self.notice_displayed = False
        self.VERSION = __version__                
        # Display notice only once
        if not self.notice_displayed:
            self._start()
    
    def _start(self):
        """Display version information and update notice.

        Prints information about the current version of PySDBots and displays a notification if a newer version is available.

        This method checks the latest available version of PySDBots by querying a remote configuration source.
        """
        # Set notice_displayed flag to True
        self.notice_displayed = True
        year = date.today().year
        # Print version information
        print(
            f'TeraboxDL v{__version__}, Copyright (C) '
            f'{year} Damantha Jasinghe <https://github.com/Damantha126>\n'
            'Licensed under the terms of the MIT License, '
            'Massachusetts Institute of Technology (MIT)\n',
        )
        # Check for newer version and print update notice
        if req["LAST_VERSION"] != __version__:
            text = f'Update Available!\n' \
                    f'New TeraboxDL v{req["LAST_VERSION"]} ' \
                    f'is now available!\n'
            if not sys.platform.startswith('win'):
                    print(f'\033[93m{text}\033[0m')
            else:
                print(text)

    def version(self):
        return(self.VERSION)
    
    @staticmethod
    def _get_formatted_size(size_bytes: int) -> str:
        """
        Convert file size in bytes to a human-readable format.

        Args:
            size_bytes (int): File size in bytes.

        Returns:
            str: Human-readable file size.
        """
        if size_bytes >= 1024 * 1024:
            size = size_bytes / (1024 * 1024)
            unit = "MB"
        elif size_bytes >= 1024:
            size = size_bytes / 1024
            unit = "KB"
        else:
            size = size_bytes
            unit = "bytes"
        return f"{size:.2f} {unit}"

    @staticmethod
    def _find_between(s: str, start: str, end: str) -> str:
        """
        Extract a substring between two markers.

        Args:
            s (str): The string to search.
            start (str): The starting marker.
            end (str): The ending marker.

        Returns:
            str: The extracted substring.
        """
        start_index = s.find(start) + len(start)
        end_index = s.find(end, start_index)
        if start_index == -1 or end_index == -1:
            return ""
        return s[start_index:end_index]

    def get_file_info(self, link: str, direct_url: bool = False) -> dict:
        """
        Retrieve file information from Terabox.

        Args:
            link (str): The Terabox link to retrieve file information for.
            direct_url (bool): Whether to return a direct download link.

        Returns:
            dict: A dictionary containing file information.
        """
        try:
            if not link:
                return {"error": "Link cannot be empty."}

            # First request
            temp_req = requests.get(link, headers=self.headers)
            if not temp_req.ok:
                return {"error": "Failed to fetch the initial link."}

            # Parse URL and check for 'surl' parameter
            parsed_url = urlparse(temp_req.url)
            query_params = parse_qs(parsed_url.query)
            if "surl" not in query_params:
                return {"error": "Invalid link. Please check the link."}

            # Second request
            req = requests.get(temp_req.url, headers=self.headers)
            respo = req.text

            # Extract tokens
            js_token = self._find_between(respo, 'fn%28%22', '%22%29')
            logid = self._find_between(respo, 'dp-logid=', '&')
            bdstoken = self._find_between(respo, 'bdstoken":"', '"')

            if not js_token or not logid or not bdstoken:
                raise Exception("Failed to extract required tokens.")

            surl = query_params["surl"][0]
            params = {
                "app_id": "250528",
                "web": "1",
                "channel": "dubox",
                "clienttype": "0",
                "jsToken": js_token,
                "dp-logid": logid,
                "page": "1",
                "num": "20",
                "by": "name",
                "order": "asc",
                "site_referer": temp_req.url,
                "shorturl": surl,
                "root": "1,",
            }

            # Third request to get file list
            req2 = requests.get("https://www.terabox.app/share/list", headers=self.headers, params=params)
            response_data2 = req2.json()

            if (
                not response_data2 or
                "list" not in response_data2 or
                not response_data2["list"] or
                response_data2.get("errno")
            ):
                raise Exception("Failed to retrieve file list.")

            if direct_url:
                # Get direct link
                direct_link_response = requests.head(
                    response_data2["list"][0]["dlink"],
                    headers=self.headers,
                    allow_redirects=True
                )
                direct_link = direct_link_response.url
            return {
                "file_name": response_data2["list"][0]["server_filename"],
                "download_link": response_data2["list"][0]["dlink"] if not direct_url else direct_link,
                "thumbnail": response_data2["list"][0]["thumbs"]["url3"],
                "file_size": self._get_formatted_size(int(response_data2["list"][0]["size"])),
                "sizebytes": int(response_data2["list"][0]["size"]),
            }
        except:
            return {"error": "An error occurred while retrieving file information."}
    
    def download(self, file_info: dict, save_path=None, callback=None) -> dict:
        """
        Download a file from Terabox using the provided file information.

        Args:
            file_info (dict): A dictionary containing file information, including the download link and file name.
            save_path (str, optional): The directory path where the file should be saved. Defaults to the current directory.
            callback (callable, optional): A callback function that receives progress updates with parameters (downloaded_bytes, total_bytes, percentage)

        Returns:
            dict: A dictionary containing the file path or an error message.
        """
        session = requests.Session()
        try:
            # Validate file_info
            if not isinstance(file_info, dict):
                return {"error": "Invalid file_info format. Expected a dictionary."}
            if "file_name" not in file_info or "download_link" not in file_info:
                return {"error": "file_info must contain 'file_name' and 'download_link' keys."}

            # Determine the file save path
            if save_path:
                try:
                    os.makedirs(save_path, exist_ok=True)
                    if os.path.isdir(save_path):
                        file_path = os.path.join(save_path, file_info["file_name"])
                    else:
                        return {"error": "Provided save_path is not a directory."}
                except Exception as e:
                    return {"error": f"Invalid save_path: {e}"}
            else:
                file_path = file_info["file_name"]

            # Start downloading the file
            with session.get(file_info["download_link"], headers=self.dlheaders, stream=True) as response:
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))
                block_size = 8192  # 8 KB

                # Write the file in chunks
                with open(file_path, 'wb') as file:
                    downloaded = 0

                    # Create tqdm progress bar if no callback is provided
                    if callback is None:
                        pbar = tqdm.tqdm(total=total_size, unit='B', unit_scale=True, 
                                        desc=f"Downloading {file_info['file_name']}")
                        
                    for chunk in response.iter_content(chunk_size=block_size):
                        if chunk:
                            file.write(chunk)
                            downloaded += len(chunk)

                            # Update progress
                            percentage = (downloaded / total_size) * 100 if total_size > 0 else 0
                            
                            if callback:
                                callback(downloaded, total_size, percentage)
                            else:
                                pbar.update(len(chunk))
                    if callback is None:
                        pbar.close()

                print(f"\nDownload complete: {file_path}")
                return {"file_path": file_path}

        except requests.RequestException as e:
            return {"error": f"Request error occurred: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}