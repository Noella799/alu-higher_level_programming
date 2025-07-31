#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
using the urllib package and displays the response body.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except urllib.error.URLError as e:
        print("Error:", e.reason)
