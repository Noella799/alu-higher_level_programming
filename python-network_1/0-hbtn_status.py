#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib package
and displays specific information about the response body.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))  # Removed b'' formatting
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
