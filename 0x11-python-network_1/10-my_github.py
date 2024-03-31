#!/usr/bin/python3
''' This scripts handles JSON responses '''

if __name__ == '__main__':

    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    creds = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    r = requests.get('https://api.github.com/user', auth=creds)

    print(r.json().get('id')
