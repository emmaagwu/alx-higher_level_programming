#!/usr/bin/python3
''' This scripts handles http error codes '''

if __name__ == '__main__':

    import sys
    import requests

    r = requests.get(sys.argv[1])

    if r.status_code > 400:
        print('Error code: {}'.format(r.status_code))

    else:
        print(r.text)
