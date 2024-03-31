#!/usr/bin/python3
''' This script makes a request with custom parameters '''

if __name__ == '__main__':

    import sys
    import requests

    email = {"email": sys.argv[2]}

    r = requests.post(sys.argv[1], data=email)

    print(r.text)
