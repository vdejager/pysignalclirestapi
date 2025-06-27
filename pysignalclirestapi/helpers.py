"""Helper functions"""

import base64
import requests
from sys import version_info

def bytes_to_base64(in_bytes: bytes) -> str:
    """Converts bytes to base64-encoded str using the appropriate system version.
    """
    if version_info >= (3, 0):
        return str(base64.b64encode(in_bytes), encoding="utf-8")
    else:
        return str(base64.b64encode(in_bytes)).encode("utf-8")


import requests

def read_file(source):
    if source.startswith('http://') or source.startswith('https://'):
        # Read from URL
        response = requests.get(source)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.content
    else:
        # Read from disk
        with open(source, 'rb') as file:
            return file.read()