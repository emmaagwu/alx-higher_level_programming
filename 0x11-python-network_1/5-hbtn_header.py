#!/usr/bin/python3
''' This scripts make a request and gets a header response variable '''

if __name__ == '__main__':

    import requests
    import sys

    r = requests.get(sys.argv[1])

    print(r.headers.get('X-Request-Id'))
