#!/usr/bin/python3
''' This module is a script to connect to a MySQL database'''


if __name__ == '__main__':
    import MySQLdb
    import sys

    db = (MySQLdb.connect(host='localhost', user=sys.argv[1],
          passwd=sys.argv[2], db=sys.argv[3], port=3306))

    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE BINARY "N%"')

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
