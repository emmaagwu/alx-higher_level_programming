#!/usr/bin/python3
''' This scripts handles JSON responses '''

if __name__ == '__main__':

    import sys
    import requests

    q = '' if len(sys.argv) < 2 else sys.argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        res = r.json()
        if res == {}:
            print('No result')

        else:
            print('[{}] {}'.format(res.get('id'), res.get('name')))

    except ValueError:
        print('Not a valid JSON')
