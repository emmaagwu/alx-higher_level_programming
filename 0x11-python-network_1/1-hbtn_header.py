#!/usr/bin/python3
''' This  takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id '''

if __name__ == '__main__':

    import sys
    from urllib.request import urlopen

    with urlopen(sys.argv[1]) as req:
        headers = req.getheaders()

        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
