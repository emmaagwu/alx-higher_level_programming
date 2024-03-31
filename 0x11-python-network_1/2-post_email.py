#!/usr/bin/python3
''' This script makes a post request to a given site
with an email variable  and displays the response body '''

if __name__ == '__main__':

    import sys
    from urllib.request import urlopen, Request
    from urllib import parse

    email = sys.argv[2]
    site = sys.argv[1]

    data = parse.urlencode({'email': email})
    data = data.encode('ascii')

    req = Request(site, data)

    with urlopen(req) as response:
        response = response.read()
        print(response.decode('utf-8'))
