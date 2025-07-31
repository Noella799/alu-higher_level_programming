
#!/usr/bin/python3
"""
Fetches status from either:
- https://intranet.hbtn.io/status (primary)
- http://0.0.0.0:5050/status (fallback)
using requests package and displays response information.
"""

import requests

if __name__ == "__main__":
    urls = [
        'https://intranet.hbtn.io/status',
        'http://0.0.0.0:5050/status'
    ]
    
    for url in urls:
        try:
            response = requests.get(url)
            print("Body response:")
            print("\t- type: {}".format(type(response.text)))
            print("\t- content: {}".format(response.text))
            break
        except requests.exceptions.RequestException:
            continue
