#!/usr/bin/python3
''' This script catches http errors and displays them '''

if __name__ == '__main__':

    import sys
    from urllib.request import urlopen
    from urllib.error import HTTPError, URLError

    try:
        with urlopen(sys.argv[1]) as res:
            res = res.read()
            print(res.decode('utf-8'))

    except HTTPError as e:
        print('Error code: {}'.format(e.code))
