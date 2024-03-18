#!/usr/bin/python3
''' This module is a script to connect to a MySQL database'''


if __name__ == '__main__':
    import MySQLdb
    import sys

    if (len(sys.argv) == 4):

        db = (MySQLdb.connect(host='localhost', user=sys.argv[1],
              passwd=sys.argv[2], db=sys.argv[3], port=3306))

        cur = db.cursor()
        cur.execute('SELECT cities.id, cities.name, states.name FROM\
                     cities, states WHERE cities.state_id=states.id')

        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        db.close()
