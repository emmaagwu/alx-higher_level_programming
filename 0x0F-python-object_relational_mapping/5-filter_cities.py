#!/usr/bin/python3
''' This module is a script to connect to a MySQL database'''


if __name__ == '__main__':
    import MySQLdb
    import sys

    if (len(sys.argv) == 5):

        db = (MySQLdb.connect(host='localhost', user=sys.argv[1],
              passwd=sys.argv[2], db=sys.argv[3], port=3306))

        cur = db.cursor()
        cur.execute('SELECT cities.name FROM cities INNER JOIN\
                     states ON cities.state_id=states.id\
                     WHERE states.name=%s', (sys.argv[4],))

        rows = cur.fetchall()
        values = [row[0] for row in rows]
        print(*values, sep=', ')

        cur.close()
        db.close()
