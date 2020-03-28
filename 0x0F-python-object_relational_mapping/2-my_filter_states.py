#!/usr/bin/python3
""" Select all states where bname ord by id """

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states\
            WHERE BINARY name = '{}' ORDER BY id".format(argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)